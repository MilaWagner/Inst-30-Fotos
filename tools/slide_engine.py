"""Движок «видеослайд» (9:16 для TikTok) в стиле роликов Милы:
чередование цветных/кремовых слайдов, аватарка + ник, жирный заголовок с курсивом,
наклонные карточки/плашки/фото, чёрная плашка с подсветкой слов, полоска прогресса.
Терракота заменена на пастельно-коричневый. Кадры Pillow -> ffmpeg."""
import math, re, subprocess, sys, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = "/tmp/claude-0/-home-user-Inst-30-Fotos/8eb0e0d4-3d28-5e23-be55-de9797cd7607/scratchpad/"
U = "/root/.claude/uploads/8eb0e0d4-3d28-5e23-be55-de9797cd7607/"
FONTS = S + "fonts/"
W, H, FPS = 1080, 1920, 25
HANDLE = "@la.vita.libera"

BG = {"brown": (201, 170, 144), "cream": (241, 234, 223)}
INK = (23, 23, 23)
ITAL = {"brown": (247, 240, 229), "cream": (160, 108, 78)}
CARD_CREAM = (243, 236, 226); CARD_DARK = (23, 23, 23); BROWN_LIGHT = (214, 180, 150)
GREY = (125, 125, 125)

_f = {}
def font(name, size):
    k = (name, size)
    if k not in _f: _f[k] = ImageFont.truetype(FONTS + name, size)
    return _f[k]
HB = lambda s: font("Manrope_800ExtraBold.ttf", s)
HI = lambda s: font("PlayfairDisplay_600SemiBold_Italic.ttf", s)

PHOTOS = {1: "b81d2287-image.jpg", 2: "782aafa9-image.jpg", 3: "71ef4252-image.jpg", 4: "981fd6ff-image.jpg",
          5: "b022bf0d-image.jpg", 6: "1af253e2-image.jpg", 7: "e7b84ece-image.jpg", 8: "b5cc2dd1-image.jpg"}
FOCUS = {1: (.5, .38), 2: (.5, .40), 3: (.5, .38), 4: (.62, .55), 5: (.52, .38), 6: (.45, .45), 7: (.62, .45), 8: (.62, .70)}
_img = {}
def photo_img(pid):
    if pid not in _img: _img[pid] = Image.open(U + PHOTOS[pid]).convert("RGB")
    return _img[pid]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(t): t = clamp(t); return 1 - (1 - t) ** 3
def back(t, c1=1.4):
    t = clamp(t); c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

# ---------- слои ----------
def shadow_wrap(im, blur=22, off=16, alpha=85):
    pad = blur * 3
    out = Image.new("RGBA", (im.width + pad * 2, im.height + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", out.size, (0, 0, 0, 0))
    mask = im.getchannel("A")
    blk = Image.new("RGBA", im.size, (40, 30, 24, alpha)); blk.putalpha(mask.point(lambda v: int(v * alpha / 255)))
    sh.alpha_composite(blk, (pad, pad + off)); sh = sh.filter(ImageFilter.GaussianBlur(blur))
    out.alpha_composite(sh); out.alpha_composite(im, (pad, pad))
    return out

def rrect(size, r, fill):
    im = Image.new("RGBA", size, (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), r, fill=fill)
    return im

def put(base, layer, cx, cy, scale=1.0, angle=0, alpha=1.0):
    if scale <= 0.02 or alpha <= 0.01: return
    im = layer
    if scale != 1.0: im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if angle: im = im.rotate(angle, resample=Image.BICUBIC, expand=True)
    if alpha < 1.0:
        a = im.getchannel("A").point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def text_w(txt, f): return f.getlength(txt)

def pill_layer(txt, size=50, fill=CARD_DARK, color=(246, 240, 230), padx=46, h=104, strike=0.0, sc=INK):
    f = HB(size); w = int(text_w(txt, f)) + padx * 2
    im = rrect((w, h), h // 2, fill + (255,)); d = ImageDraw.Draw(im)
    d.text((w / 2, h / 2 + 2), txt, font=f, fill=color, anchor="mm")
    if strike > 0:
        d.line((padx - 10, h / 2, padx - 10 + (w - 2 * padx + 20) * clamp(strike), h / 2), fill=(200, 70, 60), width=9)
    return shadow_wrap(im, 16, 10, 70)

def card_layer(big, small, dark=False, w=450, h=300):
    im = rrect((w, h), 38, (CARD_DARK if dark else CARD_CREAM) + (255,)); d = ImageDraw.Draw(im)
    col = BROWN_LIGHT if dark else INK
    bs = 84
    while text_w(big, HB(bs)) > w - 60 and bs > 30: bs -= 2
    d.text((w / 2, h / 2 - 18), big, font=HB(bs), fill=col, anchor="mm")
    d.text((w / 2, h / 2 + 66), small, font=HB(40), fill=(246, 240, 230) if dark else (95, 85, 78), anchor="mm")
    return shadow_wrap(im, 22, 16, 80)

def photo_layer(pid, w=470, h=600):
    im = photo_img(pid); iw, ih = im.size; fx, fy = FOCUS[pid]
    tw = w / h
    if iw / ih > tw: cw, ch = ih * tw, ih
    else: cw, ch = iw, iw / tw
    x0 = min(max(fx * iw - cw / 2, 0), iw - cw); y0 = min(max(fy * ih - ch / 2, 0), ih - ch)
    ph = im.resize((w, h), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch)).convert("RGBA")
    bw = 14
    fr = rrect((w + bw * 2, h + bw * 2), 40, (246, 240, 230, 255))
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), 28, fill=255)
    fr.paste(ph, (bw, bw), m)
    return shadow_wrap(fr, 26, 20, 95)

_av = None
def avatar():
    global _av
    if _av is None:
        im = photo_img(2); iw, ih = im.size
        cx, cy, r = 0.43 * iw, 0.38 * ih, 0.20 * iw
        a = im.crop((int(cx - r), int(cy - r), int(cx + r), int(cy + r))).resize((88, 88), Image.LANCZOS).convert("RGBA")
        m = Image.new("L", (88, 88), 0); ImageDraw.Draw(m).ellipse((0, 0, 87, 87), fill=255)
        o = Image.new("RGBA", (96, 96), (246, 240, 230, 255)); mm = Image.new("L", (96, 96), 0)
        ImageDraw.Draw(mm).ellipse((0, 0, 95, 95), fill=255); o.putalpha(mm); o.paste(a, (4, 4), m); _av = o
    return _av

# ---------- тайминг ----------
import os, difflib
def _norm(w): return re.sub(r"[^\wа-яё%-]", "", w.lower())

def whisper_align(num, words, fallback):
    data = json.load(open(os.path.join(os.path.dirname(__file__), "words.json")))[str(num)]
    wh = [(a, b, w) for a, b, w in data if _norm(w)]
    A = [_norm(w) for w in words]; Bn = [_norm(w[2]) for w in wh]
    sm = difflib.SequenceMatcher(None, A, Bn, autojunk=False)
    start = [None] * len(words); end = [None] * len(words)
    for i, j, n in sm.get_matching_blocks():
        for k in range(n):
            start[i + k] = wh[j + k][0]; end[i + k] = wh[j + k][1]
    # интерполяция пропусков
    n = len(words)
    for i in range(n):
        if start[i] is None:
            l = i - 1
            while l >= 0 and start[l] is None: l -= 1
            r = i + 1
            while r < n and start[r] is None: r += 1
            lt = end[l] if l >= 0 else fallback[0][0]
            rt = start[r] if r < n else fallback[-1][1]
            span = r - l
            start[i] = lt + (rt - lt) * (i - l) / span
            end[i] = lt + (rt - lt) * (i - l + 0.8) / span
    return [(a, b) for a, b in zip(start, end)]

def audio_dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]).decode())

def speech_intervals(audio):
    dur = audio_dur(audio)
    out = subprocess.run(["ffmpeg", "-hide_banner", "-i", audio, "-af", "silencedetect=noise=-32dB:d=0.12", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    sil = []
    for i, s in enumerate(starts):
        e = ends[i] if i < len(ends) else dur
        sil.append((s, e))
    sp, t = [], 0.0
    for s, e in sil:
        if s - t > 0.05: sp.append((t, s))
        t = e
    if dur - t > 0.05: sp.append((t, dur))
    return sp, dur, sil

def word_times(words, sp):
    wts = [len(w) + (2 if re.search(r"[.?!]$", w) else 0) for w in words]
    C = sum(wts); T = sum(e - s for s, e in sp)
    def at(frac):
        x = frac * T
        for s, e in sp:
            if x <= e - s: return s + x
            x -= e - s
        return sp[-1][1]
    res, c = [], 0
    for w, wt in zip(words, wts):
        res.append((at(c / C), at((c + wt) / C))); c += wt
    return res

def sentences(text):
    return [s for s in re.split(r"(?<=[.?!])\s+", text.strip()) if s]

# ---------- сцена ----------
class Video:
    def __init__(self, num, text, audio, scenes, out):
        self.num, self.audio, self.scenes, self.out = num, audio, scenes, out
        self.sents = sentences(text)
        self.words, self.sent_of = [], []
        for i, s in enumerate(self.sents):
            for w in s.split():
                self.words.append(w); self.sent_of.append(i)
        sp, self.dur, sil = speech_intervals(audio)
        est = word_times(self.words, sp)
        # граница предложения = ближайшая к оценке пауза
        cand = [x for x in sil if x[1] - x[0] >= 0.15 and x[0] > 0.2 and x[1] < self.dur - 0.1]
        bounds, used = [], -1
        for si in range(len(self.sents) - 1):
            last = max(i for i, v in enumerate(self.sent_of) if v == si)
            e = est[last][1]
            best = None
            for j, (a, b) in enumerate(cand):
                if j <= used: continue
                dd = abs(a - e)
                if dd < 1.6 and (best is None or dd < best[0]): best = (dd, j)
            if best: used = best[1]; bounds.append(cand[best[1]])
            else: bounds.append((e, e + 0.05))
        segs, prev = [], 0.0
        for bi, bnd in enumerate(bounds + [(sp[-1][1], sp[-1][1])]):
            segs.append((prev, bnd[0])); prev = bnd[1]
        self.wt = [None] * len(self.words)
        for si, (a, b) in enumerate(segs):
            idx = [i for i, v in enumerate(self.sent_of) if v == si]
            sub = [(max(x, a), min(y, b)) for x, y in sp if min(y, b) - max(x, a) > 0.03] or [(a, b)]
            res = word_times([self.words[i] for i in idx], sub)
            for i, r in zip(idx, res): self.wt[i] = r
        try:
            self.wt = whisper_align(self.num, self.words, self.wt)
        except FileNotFoundError:
            pass
        first_word = {}
        for i, si in enumerate(self.sent_of): first_word.setdefault(si, i)
        self.starts = []
        for sc in scenes:
            a = sc["sents"][0]
            self.starts.append(0.0 if not self.starts else self.wt[first_word[a]][0] - 0.05)
        self.ends = self.starts[1:] + [self.dur + 0.5]
        # куски подписи
        self.chunks, cur = [], []
        for i, w in enumerate(self.words):
            if cur and (sum(len(self.words[x]) + 1 for x in cur) + len(w) > 30 or self.sent_of[cur[-1]] != self.sent_of[i]):
                self.chunks.append(cur); cur = []
            cur.append(i)
            if re.search(r"[.?!]$", w): self.chunks.append(cur); cur = []
        if cur: self.chunks.append(cur)
        self.total = self.dur + 0.5

    # --- заголовок ---
    def draw_head(self, f, sc, lt, bg):
        size0 = sc.get("hsize", 104)
        y = 480
        k_all = 0
        for line in sc["head"]:
            size = size0
            tot = sum(text_w(t, HI(size) if it else HB(size)) for t, it in line)
            if tot > 904: size = int(size * 904 / tot)
            x = 88
            for txt, it in line:
                fnt = HI(size) if it else HB(size)
                k = ease((lt - 0.05 - k_all * 0.07) / 0.35); k_all += 1
                if k > 0:
                    layer = Image.new("RGBA", (int(text_w(txt, fnt)) + 20, int(size * 1.5)), (0, 0, 0, 0))
                    ImageDraw.Draw(layer).text((10, int(size * 1.1)), txt, font=fnt, fill=(ITAL[bg] if it else INK) + (int(255 * k),), anchor="ls")
                    f.alpha_composite(layer, (int(x - 10), int(y - size * 1.1 + (1 - k) * 30)))
                x += text_w(txt, fnt)
            y += int(size0 * 1.18)

    # --- элементы ---
    def draw_el(self, f, el, lt, sdur, bg):
        t0 = el.get("at", 0.0) * sdur + 0.35
        k = lt - t0
        kind = el["k"]
        flo = math.sin(lt * 2.2 + el.get("ph", 0)) * 4
        if kind == "pills":
            x, y = el.get("x", 540), el.get("y", 760)
            for i, txt in enumerate(el["items"]):
                kk = (k - i * el.get("gap", 0.35)) / 0.45
                if kk <= 0: continue
                lay = pill_layer(txt, el.get("size", 52))
                put(f, lay, x + (el.get("dx", 0) if i % 2 else 0), y + i * el.get("step", 150) + flo, back(kk), angle=(-3 if i % 2 == 0 else 3))
        elif kind == "cross":
            x, y = el.get("x", 540), el.get("y", 760)
            for i, txt in enumerate(el["items"]):
                kk = (k - i * el.get("gap", 0.45)) / 0.4
                if kk <= 0: continue
                st = clamp((k - i * el.get("gap", 0.45) - 0.5) / 0.3)
                lay = pill_layer(txt, el.get("size", 52), fill=CARD_CREAM, color=INK, strike=st)
                put(f, lay, x, y + i * el.get("step", 150) + flo, back(kk), angle=(-2 if i % 2 == 0 else 2))
        elif kind == "cards2":
            (a1, a2), (b1, b2) = el["a"], el["b"]
            put(f, card_layer(a1, a2, False), 320, el.get("y", 860) + flo, back(k / 0.5), angle=-5)
            put(f, card_layer(b1, b2, True), 770, el.get("y", 860) + 70 - flo, back((k - 0.5) / 0.5), angle=5)
        elif kind == "photo":
            lay = photo_layer(el["pid"], el.get("w", 470), el.get("h", 600))
            put(f, lay, el.get("x", 780), el.get("y", 960) + flo, back(k / 0.55), angle=el.get("ang", 4))
        elif kind == "steps":
            x, y = 88, el.get("y", 700)
            for i, txt in enumerate(el["items"]):
                kk = (k - i * el.get("gap", 0.5)) / 0.45
                if kk <= 0: continue
                im = rrect((904, 140), 40, CARD_CREAM + (255,)) if bg == "brown" else rrect((904, 140), 40, CARD_DARK + (255,))
                d = ImageDraw.Draw(im)
                d.ellipse((24, 24, 116, 116), fill=(CARD_DARK if bg == "brown" else (201, 170, 144)) + (255,))
                d.text((70, 72), str(i + 1), font=HB(52), fill=(246, 240, 230) if bg == "brown" else INK, anchor="mm")
                d.text((150, 72), txt, font=HB(48), fill=INK if bg == "brown" else (246, 240, 230), anchor="lm")
                put(f, shadow_wrap(im, 18, 12, 70), 540, y + 70 + i * 170, back(kk), angle=(-1.5 if i % 2 == 0 else 1.5))
        elif kind == "msg":
            kk = back(k / 0.5)
            im = rrect((904, 150), 75, (255, 255, 255, 255))
            put(f, shadow_wrap(im, 20, 14, 70), 540, el.get("y", 820), kk)
            word = el["word"]; n = int(clamp((k - 0.5) / 1.0) * len(word) + 0.001)
            if kk > 0.6:
                d = ImageDraw.Draw(f); x0 = 540 - 452 + 60
                d.text((x0, el.get("y", 820) + 2), word[:n], font=HB(76), fill=INK, anchor="lm")
                if int(lt * 2.5) % 2 == 0:
                    bx = x0 + text_w(word[:n], HB(76)) + 6
                    d.rectangle((bx, el.get("y", 820) - 40, bx + 6, el.get("y", 820) + 40), fill=(160, 108, 78))
                pul = 1 + 0.07 * math.sin(lt * 8) if k > 1.6 else clamp((k - 0.3) / 0.4)
                send = Image.new("RGBA", (116, 116), (0, 0, 0, 0)); sd = ImageDraw.Draw(send)
                sd.ellipse((0, 0, 115, 115), fill=BG["brown"] + (255,)) if bg == "cream" else sd.ellipse((0, 0, 115, 115), fill=CARD_DARK + (255,))
                sd.polygon([(36, 84), (36, 34), (88, 60)], fill=(246, 240, 230))
                put(f, send, 540 + 452 - 80, el.get("y", 820), pul)
        elif kind == "bars":
            y = el.get("y", 740)
            for i, (lab, fr, dark) in enumerate(el["rows"]):
                kk = (k - i * 0.5) / 0.4
                if kk <= 0: continue
                d = ImageDraw.Draw(f)
                d.text((88, y + i * 210), lab, font=HB(46), fill=INK, anchor="ls")
                bw = int(904 * fr * ease((k - i * 0.5 - 0.2) / 0.9))
                if bw > 30:
                    bar = rrect((bw, 84), 28, (CARD_DARK if dark else (CARD_CREAM if bg == "brown" else BG["brown"])) + (255,))
                    f.alpha_composite(bar, (88, y + i * 210 + 24))

    # --- кадр ---
    def frame(self, t):
        si = max(i for i, s in enumerate(self.starts) if t >= s - 1e-6)
        sc = self.scenes[si]; lt = t - self.starts[si]; sdur = self.ends[si] - self.starts[si]
        bg = sc["bg"]
        f = Image.new("RGBA", (W, H), BG[bg] + (255,))
        # лёгкий въезд сцены
        d = ImageDraw.Draw(f)
        f.alpha_composite(avatar(), (88, 175))
        d.text((200, 223), HANDLE, font=HB(36), fill=INK, anchor="lm")
        self.draw_head(f, sc, lt, bg)
        for el in sc.get("els", []): self.draw_el(f, el, lt, sdur, bg)
        # плашка с подписью
        bar = rrect((904, 124), 40, CARD_DARK + (255,)); f.alpha_composite(shadow_wrap(bar, 14, 10, 60), (88 - 42, 1360 - 42))
        ci = None
        for i, ch in enumerate(self.chunks):
            if self.wt[ch[0]][0] - 0.03 <= t: ci = i
        if ci is not None:
            ch = self.chunks[ci]; fnt = HB(46)
            full = " ".join(self.words[i] for i in ch); total = text_w(full, fnt)
            x = 540 - total / 2; d = ImageDraw.Draw(f)
            for i in ch:
                w = self.words[i] + " "
                col = (246, 240, 230) if t >= self.wt[i][0] - 0.02 else GREY
                d.text((x, 1422), w, font=fnt, fill=col, anchor="lm"); x += text_w(w, fnt)
        # прогресс
        p = clamp(t / self.total)
        track = (255, 255, 255, 70) if bg == "brown" else (200, 192, 180, 255)
        d = ImageDraw.Draw(f); d.rounded_rectangle((88, 1536, 992, 1544), 4, fill=track)
        d.rounded_rectangle((88, 1536, 88 + 904 * p, 1544), 4, fill=CARD_DARK + (255,))
        return f.convert("RGB")

    def render(self):
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
               "-i", "-", "-i", self.audio, "-t", f"{self.total:.2f}", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
               "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", self.out]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for i in range(int(self.total * FPS)): p.stdin.write(self.frame(i / FPS).tobytes())
        p.stdin.close(); p.wait(); print(self.out)

    def preview(self, times, name):
        ims = [self.frame(t).resize((360, 640)) for t in times]
        sheet = Image.new("RGB", (360 * len(ims), 640))
        for i, im in enumerate(ims): sheet.paste(im, (360 * i, 0))
        sheet.save(S + name, quality=88)

"""Ольга (FitLine), ролик без лица «Магний и судороги» в стиле «видеослайд».
Голос: офлайн-синтез Piper (ru_RU-irina-medium). Запуск: python3 -I olga_magnij.py [prev]"""
import os, sys, subprocess
sys.path.insert(0, "/home/user/Inst-30-Fotos/tools")
from PIL import Image, ImageDraw, ImageFont
import slide_engine as E
import math
from PIL import ImageFilter

SP = "/tmp/claude-0/-home-user-Inst-30-Fotos/c86b70d5-0211-5bc8-9062-180e9641e68c/scratchpad/"
OUT = "/home/user/Inst-30-Fotos/videos/"
VOICE = SP + "piper/ru_RU-irina-medium.onnx"
os.makedirs(OUT, exist_ok=True); os.makedirs(SP + "audio", exist_ok=True)

# --- настройка движка под Ольгу: шрифты, без фото, монограмма вместо аватарки ---
E.S = SP
_vf = {}
def _var(path, size, wght):
    k = (path, size, wght)
    if k not in _vf:
        f = ImageFont.truetype(path, size); f.set_variation_by_axes([wght]); _vf[k] = f
    return _vf[k]
E.HB = lambda s: _var(SP + "fonts/Manrope%5Bwght%5D.ttf", s, 800)
E.HI = lambda s: _var(SP + "fonts/PlayfairDisplay-Italic%5Bwght%5D.ttf", s, 600)
E.HANDLE = "Ольга · энергия каждый день"

# ---------- стиль Ольги: кремовая бумага, акварельные розы, шалфей ----------
SAGE = (122, 148, 108); BLUSH = (241, 184, 178); PEACH = (247, 200, 168); MAUVE = (146, 98, 92)
E.BG = {"brown": (246, 236, 228), "cream": (250, 246, 239)}
E.INK = (84, 68, 62)
E.ITAL = {"brown": MAUVE, "cream": SAGE}
E.CARD_DARK = SAGE; E.CARD_CREAM = (255, 252, 247); E.BROWN_LIGHT = (252, 232, 222); E.GREY = (205, 218, 196)
E.HB = lambda s: _var(SP + "fonts/Manrope%5Bwght%5D.ttf", s, 700)
_pill = E.pill_layer
def _pill_olga(txt, size=50, fill=None, color=None, **k):
    return _pill(txt, size, fill or E.CARD_CREAM, color or E.INK, **k)
E.pill_layer = _pill_olga

def _rose(r, base, seed):
    import random; rnd = random.Random(seed)
    im = Image.new("RGBA", (r * 4, r * 4), (0, 0, 0, 0)); c = r * 2
    for i in range(9):
        a = rnd.uniform(0, 6.28); d_ = rnd.uniform(0.15, 0.55) * r; rr = rnd.uniform(0.45, 0.75) * r
        x, y = c + d_ * math.cos(a), c + d_ * math.sin(a)
        col = tuple(max(0, min(255, v + rnd.randint(-14, 10))) for v in base)
        lay = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(lay).ellipse((x - rr, y - rr * 0.85, x + rr, y + rr * 0.85), fill=col + (rnd.randint(130, 190),))
        im.alpha_composite(lay.filter(ImageFilter.GaussianBlur(r * 0.08)))
    d = ImageDraw.Draw(im)
    dark = (int(base[0] * 0.86), int(base[1] * 0.66), int(base[2] * 0.66))
    for i in range(4):
        rr = r * (0.42 - i * 0.09)
        d.arc((c - rr, c - rr, c + rr, c + rr), 30 + i * 70, 260 + i * 70, fill=dark + (150,), width=max(3, r // 18))
    return im.filter(ImageFilter.GaussianBlur(1.2))

def _leaf(length, ang, seed):
    im = Image.new("RGBA", (length * 2, length * 2), (0, 0, 0, 0)); c = length
    d = ImageDraw.Draw(im); w = length * 0.32
    d.ellipse((c, c - w / 2, c + length, c + w / 2), fill=SAGE + (150,))
    d.line((c, c, c + length, c), fill=tuple(int(v * 0.8) for v in SAGE) + (170,), width=3)
    return im.rotate(ang, resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(1.5))

def _decor():
    lay = Image.new("RGBA", (E.W, E.H), (0, 0, 0, 0))
    def bouquet(cx, cy, k, seed):
        for i, (dx, dy, ang, L) in enumerate([(-150, 40, 200, 150), (120, -60, 20, 140), (40, 130, 300, 120), (-60, -140, 120, 110)]):
            lf = _leaf(int(L * k), ang, seed + i); lay.alpha_composite(lf, (int(cx + dx * k - lf.width / 2), int(cy + dy * k - lf.height / 2)))
        for i, (dx, dy, r, col) in enumerate([(0, 0, 120, BLUSH), (-130, 70, 80, PEACH), (110, 80, 70, (245, 212, 200))]):
            ro = _rose(int(r * k), col, seed * 10 + i); lay.alpha_composite(ro, (int(cx + dx * k - ro.width / 2), int(cy + dy * k - ro.height / 2)))
    bouquet(1000, 90, 1.0, 1); bouquet(60, 1860, 0.9, 2); bouquet(1040, 1880, 0.6, 3)
    import random; rnd = random.Random(7)
    paper = Image.new("L", (E.W // 4, E.H // 4)); paper.putdata([rnd.randint(0, 255) for _ in range(paper.width * paper.height)])
    paper = paper.resize((E.W, E.H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(2)).point(lambda v: int(abs(v - 128) * 0.12))
    tex = Image.new("RGBA", (E.W, E.H), (150, 120, 100, 0)); tex.putalpha(paper)
    out = Image.new("RGBA", (E.W, E.H), (0, 0, 0, 0)); out.alpha_composite(tex); out.alpha_composite(lay)
    return out
DECOR = None

def _mono():
    o = Image.new("RGBA", (96, 96), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    d.ellipse((0, 0, 95, 95), fill=(246, 240, 230, 255)); d.ellipse((4, 4, 91, 91), fill=E.CARD_DARK + (255,))
    d.text((48, 50), "О", font=E.HI(56), fill=(214, 180, 150), anchor="mm")
    return o
E.avatar = _mono
VOICE_REC = SP + "audio/olga_voice_clean.wav"     # её запись (если есть)
WORDS_REC = SP + "olga_words.json"              # тайминги слов её записи (faster-whisper)
import json, difflib
def _align(num, words, fallback):
    if not (os.path.exists(VOICE_REC) and os.path.exists(WORDS_REC)): raise FileNotFoundError
    wh = [(a, b, w) for a, b, w in json.load(open(WORDS_REC)) if E._norm(w)]
    A = [E._norm(w) for w in words]; Bn = [E._norm(w[2]) for w in wh]
    start = [None] * len(words); end = [None] * len(words)
    for i, j, n in difflib.SequenceMatcher(None, A, Bn, autojunk=False).get_matching_blocks():
        for k in range(n): start[i + k], end[i + k] = wh[j + k][0], wh[j + k][1]
    n = len(words)
    for i in range(n):
        if start[i] is None:
            l = i - 1
            while l >= 0 and start[l] is None: l -= 1
            r = i + 1
            while r < n and start[r] is None: r += 1
            lt = end[l] if l >= 0 else fallback[0][0]; rt = start[r] if r < n else fallback[-1][1]
            start[i] = lt + (rt - lt) * (i - l) / (r - l); end[i] = lt + (rt - lt) * (i - l + 0.8) / (r - l)
    return list(zip(start, end))
E.whisper_align = _align


# ---------- рисованные иллюстрации (без стоков) ----------
RED = (196, 72, 62); CALM = (120, 160, 120); CREAM2 = (246, 240, 230)

def _glow(size, col, r, a):
    g = Image.new("RGBA", size, (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    cx, cy = size[0] // 2, size[1] // 2; d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col + (a,))
    return g.filter(ImageFilter.GaussianBlur(r * 0.4))

def leg_layer(lt, calm=False):
    W_, H_ = 760, 640; im = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    pulse = 0.5 + 0.5 * math.sin(lt * (3 if calm else 9))
    gc = CALM if calm else RED
    g = _glow((560, 560), gc, 120, int(110 + 120 * pulse)); im.alpha_composite(g, (380 - 280, 350 - 280))
    ink = E.CARD_DARK + (255,)
    d.rounded_rectangle((40, 140, 400, 250), 55, fill=ink)                         # бедро
    d.ellipse((330, 135, 450, 255), fill=ink)                                       # колено
    d.polygon([(345, 210), (450, 200), (440, 470), (385, 480)], fill=ink)           # голень
    d.ellipse((300, 240, 430, 440), fill=ink)                                       # икра (сзади)
    d.rounded_rectangle((370, 450, 640, 525), 38, fill=ink)                         # стопа
    d.ellipse((600, 455, 660, 520), fill=ink)
    if not calm:
        for i, (x, y, ang) in enumerate([(200, 280, 15), (210, 380, -10), (470, 300, 170)]):
            if (lt * 3 + i * 0.33) % 1 > 0.6: continue
            pts = [(0, 0), (34, 18), (14, 30), (52, 54), (24, 60), (70, 92)]
            ca, sa = math.cos(math.radians(ang)), math.sin(math.radians(ang))
            d.line([(x + px * ca - py * sa, y + px * sa + py * ca) for px, py in pts], fill=RED + (255,), width=12, joint="curve")
    else:
        for i in range(3):
            y = 230 + i * 48 + math.sin(lt * 2 + i) * 8
            d.arc((170, y, 290, y + 70), 120, 240, fill=CALM + (255,), width=9)
    return E.shadow_wrap(im, 20, 14, 60)

def mg_layer(lt):
    S_ = 620; im = Image.new("RGBA", (S_, S_), (0, 0, 0, 0)); c = S_ // 2
    im.alpha_composite(_glow((S_, S_), (214, 180, 150), 170, 120))
    for j, rot in enumerate((25, -35, 85)):
        orb = Image.new("RGBA", (S_, S_), (0, 0, 0, 0)); od = ImageDraw.Draw(orb)
        od.ellipse((40, c - 95, S_ - 40, c + 95), outline=E.CARD_DARK + (200,), width=6)
        a = lt * (1.6 + j * 0.4) + j * 2
        ex, ey = c + (S_ / 2 - 40) * math.cos(a), c + 95 * math.sin(a)
        od.ellipse((ex - 20, ey - 20, ex + 20, ey + 20), fill=(160, 108, 78, 255))
        im.alpha_composite(orb.rotate(rot, resample=Image.BICUBIC))
    d = ImageDraw.Draw(im)
    d.ellipse((c - 130, c - 130, c + 130, c + 130), fill=E.CARD_DARK + (255,))
    d.text((c, c - 6), "Mg", font=E.HB(120), fill=CREAM2, anchor="mm")
    d.text((c + 70, c - 80), "12", font=E.HB(36), fill=(214, 180, 150), anchor="mm")
    return im

PRODUCT_PHOTO = SP + "product.png"   # сюда положить фото её продукта (PNG без фона)
def jar_layer(lt, label="мой ритуал"):
    if os.path.exists(PRODUCT_PHOTO):
        ph = Image.open(PRODUCT_PHOTO).convert("RGBA"); r = min(620 / ph.height, 640 / ph.width)
        return E.shadow_wrap(ph.resize((int(ph.width * r), int(ph.height * r)), Image.LANCZOS), 24, 18, 80)
    W_, H_ = 420, 560; im = Image.new("RGBA", (W_, H_), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((60, 110, 360, 540), 60, fill=CREAM2 + (255,), outline=E.CARD_DARK + (255,), width=8)
    d.rounded_rectangle((90, 30, 330, 130), 30, fill=E.CARD_DARK + (255,))
    d.rounded_rectangle((90, 250, 330, 420), 24, fill=(201, 170, 144, 255))
    d.text((210, 305), "Mg", font=E.HB(72), fill=E.CARD_DARK, anchor="mm")
    d.text((210, 380), label, font=E.HB(30), fill=E.CARD_DARK, anchor="mm")
    for i in range(4):
        a = lt * 1.5 + i * 1.57; x, y = 210 + 190 * math.cos(a), 300 + 230 * math.sin(a)
        s_ = 10 + 6 * math.sin(lt * 4 + i)
        d.polygon([(x, y - s_ * 2), (x + s_ / 2, y), (x, y + s_ * 2), (x - s_ / 2, y)], fill=(160, 108, 78, 255))
    return E.shadow_wrap(im, 24, 18, 80)


# ---------- стоковые клипы (Mixkit, бесплатная лицензия) ----------
STOCK = SP + "stock/"
CARD_W, CARD_H = 800, 600
def _frames(cid, w, h):
    d = STOCK + f"f_{cid}_{w}x{h}/"
    if not os.path.isdir(d):
        os.makedirs(d)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-i", STOCK + f"{cid}.mp4", "-vf",
                        f"fps=25,scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,crop={w}:{h}", "-q:v", "3", d + "%04d.jpg"], check=True)
    return sorted(os.listdir(d)), d
_fc = {}
def clip_layer(cid, t, w=CARD_W, h=CARD_H, off=0.0):
    if (cid, w, h) not in _fc: _fc[(cid, w, h)] = _frames(cid, w, h)
    fl, d = _fc[(cid, w, h)]
    i = max(0, min(int((t + off) * 25), len(fl) - 1))
    ph = Image.open(d + fl[i]).convert("RGBA")
    bw = 14; fr = E.rrect((w + bw * 2, h + bw * 2), 44, (246, 240, 230, 255))
    m = Image.new("L", (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), 32, fill=255)
    fr.paste(ph, (bw, bw), m)
    return E.shadow_wrap(fr, 26, 20, 95)

class OlgaVideo(E.Video):
    def frame(self, t):
        global DECOR
        if DECOR is None: DECOR = _decor()
        f = super().frame(t).convert("RGBA"); f.alpha_composite(DECOR)
        return f.convert("RGB")
    def draw_el(self, f, el, lt, sdur, bg):
        k = el["k"]
        if k == "clip":
            kk = E.back((lt - 0.05) / 0.45)
            if kk <= 0.02: return
            seq = el["seq"]; cid, off = seq[0][0], seq[0][2]
            for c, until, o in seq:
                cid, off = c, o
                if lt < until: break
            E.put(f, clip_layer(cid, lt, el.get("w", CARD_W), el.get("h", CARD_H), off), el.get("x", 540), el.get("y", 1000), kk, angle=el.get("ang", 0))
            return
        if k not in ("leg", "mg", "jar"): return super().draw_el(f, el, lt, sdur, bg)
        t0 = 0.15 + el.get("at", 0.0); kk = E.back((lt - t0) / 0.5)
        if kk <= 0.02: return
        x, y = el.get("x", 540), el.get("y", 1050)
        shake = math.sin(lt * 40) * 6 if (k == "leg" and not el.get("calm")) else 0
        flo = math.sin(lt * 2.2) * 6
        lay = {"leg": lambda: leg_layer(lt, el.get("calm", False)), "mg": lambda: mg_layer(lt),
               "jar": lambda: jar_layer(lt)}[k]()
        E.put(f, lay, x + shake, y + flo, kk * el.get("s", 1.0), angle=el.get("ang", 0))

TEXT = ("Вечер. Ты наконец села отдохнуть, и снова сводит ногу. Знакомо? "
        "Причин может быть несколько: мало воды, мало движения, нехватка минералов. "
        "Один из важных минералов — это магний. "
        "Он способствует нормальной работе мышц и уменьшению усталости. "
        "И нужен для нормального состояния костей и зубов. "
        "Пить его просто: один пакетик порошка развести в стакане воды и выпить маленькими глотками. "
        "Идеально — вечером, перед сном. "
        "Если судороги частые, обязательно покажись врачу. "
        "Хочешь магний, который доставляет питательные вещества прямо к клеткам? "
        "Напиши слово ХОЧУ, и я пришлю ссылку.")

def H(*lines): return [list(l) for l in lines]
B, C = "brown", "cream"
SCENES = [
 dict(sents=(0, 3), bg=B, head=H([("Сводит ", 0), ("ноги", 1)], [("по вечерам?", 0)]),
      els=[{"k": "clip", "seq": [("4548", 2.6, 1.0), ("48618", 99, -1.0)], "y": 1000, "ang": -2}]),
 dict(sents=(3, 4), bg=C, head=H([("Причин ", 0), ("несколько", 1)]),
      els=[{"k": "steps", "items": ["мало воды", "мало движения", "нехватка минералов"], "y": 760, "at": 0.05, "gap": 0.55}]),
 dict(sents=(4, 5), bg=B, head=H([("Один из них — ", 0)], [("магний", 1)]), hsize=110,
      els=[{"k": "mg", "x": 540, "y": 1040, "at": 0.05}]),
 dict(sents=(5, 7), bg=C, head=H([("Зачем ", 0), ("магний", 1)]),
      els=[{"k": "pills", "items": ["работа мышц", "меньше усталости", "кости и зубы"], "x": 540, "y": 660, "step": 120, "size": 44, "at": 0.05, "gap": 0.8}, {"k": "clip", "seq": [("36710", 99, 2.0)], "y": 1170, "h": 400, "ang": 2}]),
 dict(sents=(7, 8), bg=B, head=H([("Как ", 0), ("пить", 1)]),
      els=[{"k": "pills", "items": ["1 пакетик + стакан воды"], "x": 540, "y": 650, "size": 46, "at": 0.0}, {"k": "clip", "seq": [("47955", 3.2, 1.5), ("13198", 99, 1.0)], "y": 1080, "h": 560, "ang": -2}]),
 dict(sents=(8, 9), bg=C, head=H([("Вечером, ", 0)], [("перед сном", 1)]),
      els=[{"k": "jar", "x": 540, "y": 1030, "s": 1.25, "ang": 3, "at": 0.05}]),
 dict(sents=(9, 10), bg=B, head=H([("Часто? ", 0), ("К врачу", 1)]),
      els=[{"k": "cards2", "a": ("часто", "сводит ноги"), "b": ("врач", "обязательно"), "y": 860, "at": 0.1}]),
 dict(sents=(10, 12), bg=C, head=H([("Напиши ", 0), ("ХОЧУ", 1)]),
      els=[{"k": "msg", "word": "ХОЧУ", "y": 780, "at": 0.15}, {"k": "jar", "x": 540, "y": 1190, "s": 0.95, "ang": -3, "at": 0.6}]),
]

def voice(path):
    if os.path.exists(path): return
    subprocess.run([sys.executable, "-m", "piper", "-m", VOICE, "-f", path, "--sentence-silence", "0.35", "--length-scale", "1.05"],
                   input=TEXT.encode(), check=True)

def make():
    if os.path.exists(VOICE_REC): a = VOICE_REC
    else: a = SP + "audio/olga_magnij.wav"; voice(a)
    return OlgaVideo(0, TEXT, a, SCENES, OUT + "olga_magnij_golos.mp4")

if __name__ == "__main__" and not (len(sys.argv) > 1 and sys.argv[1] in ("music", "cover")):
    v = make()
    if len(sys.argv) > 1 and sys.argv[1] == "prev":
        ts = [(v.starts[i] + v.ends[i]) / 2 + 0.4 for i in range(len(v.scenes))]
        v.preview(ts, "olga_prev.jpg"); print([round(x, 1) for x in v.starts], round(v.dur, 1))
    else:
        v.render()

# ---------- музыка и звуки (как в add_audio.py) ----------
MUSIC = SP + "audio/music.mp3"   # её трек «Deep Liquid Bass» с Google Диска
def add_music(v, src, dst, music=MUSIC, vol=0.14):
    import add_audio as AA
    sf = SP + "audio/olga_sfx.wav"; AA.sfx_wav(v, sf); tot = v.total
    fc = (f"[1:a]aloop=loop=-1:size=2e9,atrim=0:{tot:.2f},volume={vol},afade=t=in:d=1.5,afade=t=out:st={tot-2.5:.2f}:d=2.5[m0];"
          f"[0:a]asplit=2[vo][sc];[m0][sc]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[m];"
          f"[2:a]volume=0.55[fx];[vo][m][fx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.95[a]")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", music, "-i", sf, "-filter_complex", fc,
                           "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", dst])
    print(dst)

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "music":
    v = make(); add_music(v, v.out, v.out.replace(".mp4", "_music.mp4"))

# ---------- обложка (9:16, ключевое — в центральной зоне 3:4 для сетки профиля) ----------
def cover(path_png):
    global DECOR
    if DECOR is None: DECOR = _decor()
    W, H = E.W, E.H
    f = Image.new("RGBA", (W, H), E.BG["cream"] + (255,))
    f.alpha_composite(E.avatar(), (88, 300))
    ImageDraw.Draw(f).text((200, 348), E.HANDLE, font=E.HB(40), fill=E.INK, anchor="lm")
    y = 560
    for line in [[("Сводит ", 0), ("ноги", 1)], [("по вечерам?", 0)]]:
        size = 132; x = 88; d = ImageDraw.Draw(f)
        for txt, it in line:
            fnt = E.HI(size) if it else E.HB(size)
            d.text((x, y), txt, font=fnt, fill=E.ITAL["cream"] if it else E.INK, anchor="ls"); x += E.text_w(txt, fnt)
        y += 150
    E.put(f, clip_layer("48618", 4.0, 640, 600), 400, 1060, 1.0, angle=-3)
    E.put(f, jar_layer(0.0), 800, 1230, 0.62, angle=6)
    E.put(f, E.pill_layer("магний: как пить", 50, E.CARD_DARK, (255, 252, 247)), 540, 1440, 1.0, angle=-2)
    f.alpha_composite(DECOR)
    im = f.convert("RGB"); im.save(path_png); im.save(path_png.replace(".png", ".jpg"), quality=92)
    return path_png

def with_cover(src, png, dst, secs=0.12):
    """Ставит обложку первым кадром (≈0.12 с), чтобы превью было и там, где обложку не выбрать вручную."""
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", f"{secs}", "-framerate", "25", "-i", png,
        "-f", "lavfi", "-t", f"{secs}", "-i", "anullsrc=r=44100:cl=stereo", "-i", src, "-filter_complex",
        "[0:v]scale=1080:1920,format=yuv420p,setsar=1[c];[2:v]format=yuv420p,setsar=1[m];[c][1:a][m][2:a]concat=n=2:v=1:a=1[v][a]",
        "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", dst]); print(dst)

if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "cover":
    png = cover(OUT + "olga_magnij_cover.png"); print(png)
    src = OUT + "olga_magnij_golos_music.mp4"
    if os.path.exists(src): with_cover(src, png, OUT + "olga_magnij_final.mp4")

"""Проба в стиле «студия роликов» / Демир: графика + крупная Оксана внизу кадра.
Рендер кадров Pillow -> ffmpeg. Ролик 4 «Без своего продукта»."""
import math, subprocess, sys, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = "/tmp/claude-0/-home-user-Inst-30-Fotos/8eb0e0d4-3d28-5e23-be55-de9797cd7607/scratchpad/"
AUDIO = S + "audio/v4.mp3"
OUT = "/home/user/Inst-30-Fotos/videos/proba_studio_4.mp4"
W, H, FPS = 1080, 1920, 25
DUR = 24.2

CREAM = (246, 239, 228); TEAL = (31, 95, 91); GOLD = (201, 154, 75)
BURG = (139, 38, 53); INK = (38, 38, 42); WHITE = (255, 255, 255)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ITAL = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
_fc = {}
def F(path, size):
    k = (path, size)
    if k not in _fc: _fc[k] = ImageFont.truetype(path, size)
    return _fc[k]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out(t): t = clamp(t); return 1 - (1 - t) ** 3
def back(t):
    t = clamp(t); c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

# сцены: (старт, конец) по паузам в озвучке
SC = [(0.0, 4.07), (4.07, 4.87), (4.87, 9.39), (9.39, 12.76), (12.76, 18.16), (18.16, 21.52), (21.52, DUR)]
SUB = ["Думаешь, чтобы зарабатывать онлайн, нужно придумать свой курс?", "Нет.",
       "Это самый частый миф, который держит женщин на месте годами.",
       "Зайти в диджитал можно и без своего продукта.",
       "Нужны контент, понятная система и готовность сделать первый шаг.",
       "Хочешь разобраться, с чего начать именно тебе?", "Напиши мне в личку слово ХОЧУ."]

def load_cut(fn, width, top_crop=0):
    im = Image.open(S + "cut/" + fn).convert("RGBA")
    bb = im.getchannel("A").getbbox(); im = im.crop(bb)
    r = width / im.width
    return im.resize((width, int(im.height * r)), Image.LANCZOS)
CUTS = [load_cut("c1.png", 980), load_cut("c2.png", 1000)]

def make_bg():
    bg = Image.new("RGB", (W, H), CREAM)
    blob = Image.new("L", (W, H), 0); d = ImageDraw.Draw(blob)
    d.ellipse((-300, 250, 900, 1450), fill=255); d.ellipse((500, 900, 1500, 1900), fill=140)
    blob = blob.filter(ImageFilter.GaussianBlur(160))
    tint = Image.new("RGB", (W, H), (214, 226, 220))
    return Image.composite(tint, bg, blob)
BG = make_bg()

def shadowed_card(size, radius, fill):
    pad = 40
    im = Image.new("RGBA", (size[0] + pad * 2, size[1] + pad * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    d.rounded_rectangle((pad, pad + 14, pad + size[0], pad + size[1] + 14), radius, fill=(40, 40, 40, 80))
    sh = sh.filter(ImageFilter.GaussianBlur(18)); im.alpha_composite(sh)
    d = ImageDraw.Draw(im); d.rounded_rectangle((pad, pad, pad + size[0], pad + size[1]), radius, fill=fill)
    return im

def paste_scaled(base, layer, cx, cy, scale, angle=0, alpha=1.0):
    if scale <= 0.01 or alpha <= 0: return
    im = layer
    if scale != 1: im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if angle: im = im.rotate(angle, resample=Image.BICUBIC, expand=True)
    if alpha < 1:
        a = im.getchannel("A").point(lambda v: int(v * alpha)); im = im.copy(); im.putalpha(a)
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def text_layer(txt, font, fill, stroke=0, stroke_fill=None, spacing=10, align="center"):
    d0 = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    bb = d0.multiline_textbbox((0, 0), txt, font=font, spacing=spacing, align=align, stroke_width=stroke)
    w, h = int(bb[2] - bb[0] + 40), int(bb[3] - bb[1] + 40)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.multiline_text((int(20 - bb[0]), int(20 - bb[1])), txt, font=font, fill=fill, spacing=spacing, align=align,
                     stroke_width=stroke, stroke_fill=stroke_fill)
    return im

def plate(txt, w, h, color, font_size=64, text_color=WHITE):
    im = shadowed_card((w, h), 36, color + (255,))
    t = text_layer(txt, F(SANS, font_size), text_color)
    im.alpha_composite(t, ((im.width - t.width) // 2, (im.height - t.height) // 2))
    return im

COURSE = None
def course_card():
    global COURSE
    if COURSE is None:
        c = shadowed_card((640, 420), 40, WHITE + (255,))
        d = ImageDraw.Draw(c)
        d.rounded_rectangle((70, 70, 330, 120), 14, fill=TEAL)
        for i in range(3): d.rounded_rectangle((70, 160 + i * 50, 570, 185 + i * 50), 10, fill=(226, 221, 211))
        t = text_layer("МОЙ КУРС", F(SERIF, 70), INK); c.alpha_composite(t, (c.width // 2 - t.width // 2, 330))
        COURSE = c
    return COURSE

def cross(base, cx, cy, w, h, p, color=BURG, width=26):
    p = clamp(p)
    d = ImageDraw.Draw(base)
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    q1 = clamp(p * 2); q2 = clamp(p * 2 - 1)
    if q1 > 0: d.line((x0, y0, x0 + (x1 - x0) * q1, y0 + (y1 - y0) * q1), fill=color, width=width)
    if q2 > 0: d.line((x1, y0, x1 - (x1 - x0) * q2, y0 + (y1 - y0) * q2), fill=color, width=width)

def strike(base, x0, x1, y, p, color=BURG, width=14):
    ImageDraw.Draw(base).line((x0, y, x0 + (x1 - x0) * clamp(p), y), fill=color, width=width)

def render(t):
    si = max(i for i, (a, b) in enumerate(SC) if t >= a)
    a, b = SC[si]; lt = t - a
    f = BG.convert("RGBA")
    GY = 560  # центр графической зоны
    # --- графика по сценам ---
    if si == 0:
        s = back(lt / 0.5); paste_scaled(f, course_card(), 540, GY, s)
        q = back((lt - 0.8) / 0.5); paste_scaled(f, text_layer("?", F(SERIF, 330), GOLD), 915, 470 + math.sin(lt * 5) * 8, q, angle=-12 + math.sin(lt * 3) * 6)
        paste_scaled(f, text_layer("Нужен свой курс?", F(ITAL, 86), TEAL), 540, 190, ease_out(lt / 0.5))
    elif si == 1:
        paste_scaled(f, course_card(), 540, GY, 1.0, alpha=max(0.35, 1 - lt * 1.4))
        cross(f, 540, GY, 560, 340, lt / 0.25)
        k = lt / 0.22; sc = 2.4 - 1.4 * ease_out(k) if k < 1 else 1.0
        shake = math.sin(lt * 70) * 10 * clamp(1 - lt / 0.5)
        paste_scaled(f, text_layer("НЕТ", F(SERIF, 330), BURG), 540 + shake, 960 - 330, sc, angle=-6)
    elif si == 2:
        paste_scaled(f, text_layer("МИФ", F(SERIF, 300), BURG), 540, 330, back(lt / 0.4), angle=-4)
        paste_scaled(f, text_layer("который держит на месте", F(ITAL, 64), INK), 540, 560, ease_out((lt - 0.8) / 0.5))
        for i in range(5):
            st = 1.2 + i * 0.5; p = back((lt - st) / 0.35)
            sq = shadowed_card((150, 150), 28, (TEAL if i % 2 == 0 else GOLD) + (255,))
            tt = text_layer(str(i + 1), F(SERIF, 90), WHITE); sq.alpha_composite(tt, ((sq.width - tt.width) // 2, (sq.height - tt.height) // 2))
            paste_scaled(f, sq, 120 + i * 210, 760, p)
        paste_scaled(f, text_layer("годы на одном месте", F(ITAL, 62), TEAL), 540, 900, ease_out((lt - 3.0) / 0.5))
    elif si == 3:
        pl = plate("СВОЙ ПРОДУКТ", 760, 160, (120, 120, 126), 64)
        paste_scaled(f, pl, 540, 330, back(lt / 0.4))
        d = f
        strike(f, 200, 880, 330, (lt - 0.7) / 0.35)
        pl2 = plate("DIGITAL", 760, 190, TEAL, 84)
        k = ease_out((lt - 1.3) / 0.5)
        paste_scaled(f, pl2, 540 + (1 - k) * 900, 660, 1.0)
        paste_scaled(f, text_layer("без продукта — можно", F(ITAL, 64), GOLD), 540, 860, ease_out((lt - 2.0) / 0.5))
    elif si == 4:
        items = [("КОНТЕНТ", TEAL, 0.0), ("СИСТЕМА", GOLD, 1.65), ("ПЕРВЫЙ ШАГ", BURG, 3.0)]
        for i, (txt, col, st) in enumerate(items):
            p = back((lt - st) / 0.4)
            pl = plate(txt, 800, 170, col, 66)
            paste_scaled(f, pl, 540, 250 + i * 250, p)
            if lt - st > 0.5:
                ck = ease_out((lt - st - 0.5) / 0.3)
                d = ImageDraw.Draw(f); x, y = 905, 250 + i * 250
                d.line((x - 36, y, x - 8, y + 30, x + 40, y - 34), fill=WHITE, width=16, joint="curve")
    elif si == 5:
        paste_scaled(f, text_layer("С чего начать\nименно тебе?", F(SERIF, 120), TEAL), 540, 400, back(lt / 0.5))
        for i, (x, y, sz) in enumerate([(160, 760, 150), (900, 700, 190), (700, 880, 120)]):
            paste_scaled(f, text_layer("?", F(SERIF, sz), GOLD), x, y + math.sin(lt * 3 + i) * 18, back((lt - 0.4 - i * 0.2) / 0.4), angle=math.sin(lt * 2 + i) * 14)
    else:
        paste_scaled(f, text_layer("Напиши мне в личку", F(ITAL, 96), TEAL), 540, 230, ease_out(lt / 0.5))
        box = shadowed_card((840, 150), 75, WHITE + (255,))
        paste_scaled(f, box, 500, 560, back((lt - 0.2) / 0.5))
        word = "ХОЧУ"; n = int(clamp((lt - 0.8) / 1.0) * len(word) + 0.001)
        d = ImageDraw.Draw(f)
        shown = word[:n]
        d.text((200, 560 - 52), shown, font=F(SANS, 90), fill=INK)
        if int(lt * 2.5) % 2 == 0:
            bx = 200 + d.textlength(shown, font=F(SANS, 90)) + 8; d.rectangle((bx, 510, bx + 6, 610), fill=TEAL)
        pul = 1 + 0.08 * math.sin(lt * 8) if lt > 1.8 else clamp((lt - 0.4) / 0.5)
        send = shadowed_card((130, 130), 65, GOLD + (255,)); dd = ImageDraw.Draw(send)
        dd.polygon([(40, 105), (40, 45), (105, 75)], fill=WHITE)
        paste_scaled(f, send, 930, 560, pul)
    # --- Оксана крупно внизу ---
    cut = CUTS[si % 2]
    lt_o = lt
    slide = (1 - ease_out(lt_o / 0.55)) * 500 if si in (0, 1, 2, 3, 4, 5, 6) else 0
    bob = math.sin(t * 2.2) * 6
    top = H - 760 + slide + bob
    f.alpha_composite(cut, (int((W - cut.width) / 2), int(top))) if top < H else None
    # --- субтитр над Оксаной ---
    sub = textwrap.fill(SUB[si], 26)
    sl = text_layer(sub, F(SANS, 50), WHITE, spacing=10)
    ph = shadowed_card((sl.width + 40, sl.height + 10), 34, TEAL + (255,))
    ph.alpha_composite(sl, (40 + 20, 40 + 5))
    k = ease_out(lt / 0.3)
    paste_scaled(f, ph, 540, 1140 - (1 - k) * 40, 1.0, alpha=k)
    return f.convert("RGB")

def main(preview_times=None):
    if preview_times:
        for t in preview_times:
            render(t).save(S + f"prev_{t:.1f}.jpg", quality=88)
        return
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", AUDIO, "-t", f"{DUR}", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(int(DUR * FPS)):
        p.stdin.write(render(i / FPS).tobytes())
    p.stdin.close(); p.wait(); print(OUT)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "prev":
        main([float(x) for x in sys.argv[2:]])
    else:
        main()

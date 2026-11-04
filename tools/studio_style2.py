"""Проба 2: стиль профиля @la.vita.libera — крупное тёплое фото, серифная надпись с золотым курсивом.
Ролик 4 «Без своего продукта». Кадры Pillow -> ffmpeg."""
import math, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

S = "/tmp/claude-0/-home-user-Inst-30-Fotos/8eb0e0d4-3d28-5e23-be55-de9797cd7607/scratchpad/"
U = "/root/.claude/uploads/8eb0e0d4-3d28-5e23-be55-de9797cd7607/"
AUDIO = S + "audio/v4.mp3"
OUT = "/home/user/Inst-30-Fotos/videos/proba_stil2_4.mp4"
W, H, FPS, DUR = 1080, 1920, 25, 24.2

SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_BI = "/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
CREAM = (250, 244, 233); GOLD = (232, 190, 110); TEAL = (31, 95, 91)
_fc = {}
def F(p, s):
    if (p, s) not in _fc: _fc[(p, s)] = ImageFont.truetype(p, s)
    return _fc[(p, s)]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(t): t = clamp(t); return 1 - (1 - t) ** 3

SC = [(0.0, 4.07), (4.07, 4.87), (4.87, 9.39), (9.39, 12.76), (12.76, 18.16), (18.16, 21.52), (21.52, DUR)]
# фото (файл, центр кропа x,y), направление зума
PH = [("782aafa9-image.jpg", .5, .42), ("b81d2287-image.jpg", .5, .38), ("71ef4252-image.jpg", .5, .40),
      ("1af253e2-image.jpg", .45, .45), ("71ef4252-image.jpg", .5, .40), ("782aafa9-image.jpg", .5, .42),
      ("b81d2287-image.jpg", .5, .38)]
# текст сцены: список строк, слово с * = курсив золотом
TXT = [["Думаешь, нужен", "*свой курс?*"], ["*Нет.*"], ["Это самый частый", "*миф*"],
       ["Зайти в digital можно", "*без своего продукта*"], ["*Контент.*", "Система.", "Первый шаг."],
       ["С чего начать", "*именно тебе?*"], ["Напиши мне слово", "*ХОЧУ*"]]
SMALL = [None, None, "который держит женщин на месте годами", None, "и готовность сделать первый шаг", None,
         "в личку — я расскажу подробнее"]

IMG = {}
def photo(fn):
    if fn not in IMG:
        im = Image.open(U + fn).convert("RGB")
        im = ImageEnhance.Color(im).enhance(1.08)
        im = ImageEnhance.Contrast(im).enhance(1.04)
        IMG[fn] = im
    return IMG[fn]

def frame_photo(si, lt, dur):
    fn, cx, cy = PH[si]
    im = photo(fn); w, h = im.size
    target = W / H
    if w / h > target: cw, ch = h * target, h
    else: cw, ch = w, w / target
    z = 1.0 + 0.10 * clamp(lt / dur) if si % 2 == 0 else 1.10 - 0.10 * clamp(lt / dur)
    cw2, ch2 = cw / z, ch / z
    x0 = min(max(cx * w - cw2 / 2, 0), w - cw2); y0 = min(max(cy * h - ch2 / 2, 0), h - ch2)
    return im.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw2, y0 + ch2))

def gradient():
    g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); px = g.load()
    start = int(H * 0.50)
    for y in range(start, H):
        a = int(215 * ((y - start) / (H - start)) ** 1.35)
        for x in range(0, W, 1):
            px[x, y] = (34, 22, 14, a)
    return g
GRAD = gradient()

def line_layer(words_style, font_size):
    """words_style: список (слово, курсив?) -> RGBA изображение строки."""
    fn = F(SERIF_B, font_size); fi = F(SERIF_BI, font_size)
    space = fn.getlength(" ")
    parts = []; wtot = 0
    for wd, it in words_style:
        f = fi if it else fn; l = f.getlength(wd); parts.append((wd, f, it, l)); wtot += l + space
    wtot -= space
    im = Image.new("RGBA", (int(wtot) + 80, int(font_size * 1.5)), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    x = 40
    for wd, f, it, l in parts:
        col = GOLD if it else CREAM
        d.text((x + 3, 20 + 3), wd, font=f, fill=(0, 0, 0, 110))
        d.text((x, 20), wd, font=f, fill=col)
        x += l + space
    return im

def parse(line):
    ws = []
    it = line.startswith("*") or line.endswith("*")
    for wd in line.replace("*", "").split(" "): ws.append((wd, it))
    return ws

def render(t):
    si = max(i for i, (a, b) in enumerate(SC) if t >= a)
    a, b = SC[si]; lt = t - a; dur = b - a
    base = frame_photo(si, lt, dur)
    if si > 0 and lt < 0.3:
        prev = frame_photo(si - 1, SC[si - 1][1] - SC[si - 1][0], SC[si - 1][1] - SC[si - 1][0])
        base = Image.blend(prev, base, ease(lt / 0.3))
    f = base.convert("RGBA"); f.alpha_composite(GRAD)
    d = ImageDraw.Draw(f)
    # верхний ярлык
    tag = "la vita libera"; tf = F(SERIF_BI, 46)
    d.text(((W - tf.getlength(tag)) / 2, 90), tag, font=tf, fill=(250, 244, 233, 230))
    d.line((W / 2 - 60, 160, W / 2 + 60, 160), fill=GOLD + (255,), width=3)
    # текст
    lines = TXT[si]; n = len(lines)
    size = 108 if n <= 2 else 96
    lh = int(size * 1.22)
    ytext = H - 330 - n * lh + (60 if SMALL[si] else 90)
    for i, ln in enumerate(lines):
        k = ease((lt - 0.08 - i * 0.14) / 0.4)
        if k <= 0: continue
        layer = line_layer(parse(ln), size)
        a_ = k
        if a_ < 1:
            alpha = layer.getchannel("A").point(lambda v: int(v * a_)); layer.putalpha(alpha)
        f.alpha_composite(layer, (int((W - layer.width) / 2), int(ytext + i * lh + (1 - k) * 40)))
    if SMALL[si]:
        k = ease((lt - 0.5) / 0.4)
        sm = F(SERIF_BI, 48)
        txt = SMALL[si]; tw = sm.getlength(txt)
        lay = Image.new("RGBA", (int(tw) + 40, 80), (0, 0, 0, 0)); dd = ImageDraw.Draw(lay)
        dd.text((22, 12), txt, font=sm, fill=(0, 0, 0, 120)); dd.text((20, 10), txt, font=sm, fill=(250, 244, 233, int(235 * k)))
        f.alpha_composite(lay, (int((W - lay.width) / 2), int(ytext + n * lh + 8 + (1 - k) * 20)))
    return f.convert("RGB")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "prev":
        for t in map(float, sys.argv[2:]): render(t).save(S + f"p2_{t:.1f}.jpg", quality=88)
        return
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", AUDIO, "-t", str(DUR), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
           "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", OUT]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(int(DUR * FPS)): p.stdin.write(render(i / FPS).tobytes())
    p.stdin.close(); p.wait(); print(OUT)

if __name__ == "__main__":
    main()

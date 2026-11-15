"""Движок объясняющих роликов 16:9 (1920x1080) для финансового канала без лица.
Голос: по одному mp3 на раздел сценария. Визуал: Pillow (схемы, шкалы, диаграммы), субтитры, прогресс.
Синхронизация: каждый «бит» сцены привязан к ключевой фразе текста раздела; время = доля символов * длительность.
Запуск: python3 explainer.py <episode.py> <audio_dir> <out.mp4>
"""
import json, math, os, re, subprocess, sys, importlib.util
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import character

W, H, FPS = 1920, 1080, 25
GAP = 0.7  # пауза между разделами, с
FONT_DIR = "/usr/share/fonts/opentype/inter/"

BG = (247, 244, 238); INK = (20, 33, 61); MUTED = (112, 120, 138); LINE = (226, 220, 208)
CARD = (255, 255, 255); ACC = (16, 122, 96); GOLD = (222, 160, 36); RED = (206, 64, 60)
GREEN = (36, 156, 92); BLUE = (52, 104, 214); SOFT = (236, 231, 221)
SEG = [ACC, BLUE, GOLD, (140, 100, 200), (232, 120, 80)]

# Темы оформления по рубрикам (episode.py: THEME = "sky" и т.п.). Тёмных тем нет: текст в карточках тёмный.
THEMES = {
    "cream": dict(BG=(247, 244, 238), ACC=(16, 122, 96), LINE=(226, 220, 208), SOFT=(236, 231, 221), PILL=(20, 33, 61), MOTIF=None),
    "sky":   dict(BG=(235, 242, 251), ACC=(38, 92, 196), LINE=(210, 222, 240), SOFT=(222, 232, 247), PILL=(30, 60, 130), MOTIF="dots"),
    "mint":  dict(BG=(233, 246, 240), ACC=(14, 128, 98), LINE=(205, 230, 218), SOFT=(219, 239, 229), PILL=(10, 90, 70), MOTIF="grid"),
    "blush": dict(BG=(251, 239, 234), ACC=(196, 82, 58), LINE=(240, 218, 208), SOFT=(246, 226, 218), PILL=(120, 40, 30), MOTIF="diag"),
    "lilac": dict(BG=(242, 238, 251), ACC=(112, 78, 186), LINE=(224, 216, 242), SOFT=(232, 226, 247), PILL=(70, 45, 130), MOTIF="dots"),
    "sun":   dict(BG=(252, 245, 226), ACC=(190, 120, 10), LINE=(240, 226, 190), SOFT=(246, 236, 206), PILL=(110, 70, 10), MOTIF="grid"),
}
PILL = (20, 33, 61); MOTIF = None

def apply_theme(name):
    g = globals(); t = THEMES.get(name or "cream", THEMES["cream"])
    for k, v in t.items(): g[k] = v
    g["SEG"] = [g["ACC"], BLUE, GOLD, (140, 100, 200), (232, 120, 80)]

def draw_motif(d):
    if not MOTIF: return
    col = mix(BG, LINE, .55)
    if MOTIF == "dots":
        for y in range(30, H, 60):
            for x in range(30 + (30 if (y // 60) % 2 else 0), W, 60): d.ellipse((x - 3, y - 3, x + 3, y + 3), fill=col)
    elif MOTIF == "grid":
        for x in range(0, W, 80): d.line([(x, 0), (x, H)], fill=col, width=1)
        for y in range(0, H, 80): d.line([(0, y), (W, y)], fill=col, width=1)
    elif MOTIF == "diag":
        for x in range(-H, W, 70): d.line([(x, H), (x + H, 0)], fill=col, width=2)

_fc = {}
def F(size, w="SemiBold", disp=False):
    name = ("InterDisplay-" if disp else "Inter-") + w + ".otf"
    k = (name, size)
    if k not in _fc: _fc[k] = ImageFont.truetype(FONT_DIR + name, size)
    return _fc[k]

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease(t): t = clamp(t); return 1 - (1 - t) ** 3
def mix(c1, c2, a): return tuple(int(c1[i] + (c2[i] - c1[i]) * a) for i in range(3))
def fade(c, a): return mix(BG, c, clamp(a))

class Ctx:
    """Кадр + время бита. a(d) — прогресс появления элемента с задержкой d."""
    def __init__(self, img, lt, dur):
        self.img, self.d, self.lt, self.dur = img, ImageDraw.Draw(img), lt, dur
    def a(self, delay=0.0, length=0.45): return ease((self.lt - delay) / length)

def text(c, xy, s, size, color, w="SemiBold", anchor="la", al=1.0, disp=False, dy=0):
    x, y = xy
    c.d.text((x, y + (1 - al) * 24 + dy), s, font=F(size, w, disp), fill=fade(color, al), anchor=anchor)

def rrect(c, box, r, fill, al=1.0, outline=None, width=0):
    c.d.rounded_rectangle(box, r, fill=fade(fill, al) if fill else None,
                          outline=fade(outline, al) if outline else None, width=width)

def card(c, box, al, r=28):
    x0, y0, x1, y1 = box; off = (1 - al) * 30
    c.d.rounded_rectangle((x0 + 6, y0 + 10 + off, x1 + 6, y1 + 10 + off), r, fill=fade(SOFT, al))
    c.d.rounded_rectangle((x0, y0 + off, x1, y1 + off), r, fill=fade(CARD, al), outline=fade(LINE, al), width=2)
    return off

def wrap(s, size, maxw, w="SemiBold"):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if F(size, w).getlength(t) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

# ---------- пиктограммы ----------
def person(c, cx, cy, s, col, al):
    c.d.ellipse((cx - 34 * s, cy - 120 * s, cx + 34 * s, cy - 52 * s), fill=fade(col, al))
    c.d.rounded_rectangle((cx - 62 * s, cy - 40 * s, cx + 62 * s, cy + 70 * s), 40 * s, fill=fade(col, al))

def check(c, cx, cy, r, al, ok=True):
    col = GREEN if ok else RED
    c.d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fade(col, al))
    if ok: c.d.line([(cx - r * .45, cy), (cx - r * .1, cy + r * .35), (cx + r * .5, cy - r * .35)], fill=fade(CARD, al), width=int(r * .2))
    else:
        k = r * .38
        c.d.line([(cx - k, cy - k), (cx + k, cy + k)], fill=fade(CARD, al), width=int(r * .2))
        c.d.line([(cx - k, cy + k), (cx + k, cy - k)], fill=fade(CARD, al), width=int(r * .2))

def gauge(c, y, al, marker, label=None):
    x0, x1 = 260, 1660
    zones = [(300, 580, RED), (580, 670, GOLD), (670, 740, (150, 190, 90)), (740, 800, GREEN), (800, 850, ACC)]
    for lo, hi, col in zones:
        a0 = x0 + (lo - 300) / 550 * (x1 - x0); a1 = x0 + (hi - 300) / 550 * (x1 - x0)
        c.d.rectangle((a0, y, a1, y + 44), fill=fade(col, al))
    for v in (300, 580, 670, 740, 800, 850):
        x = x0 + (v - 300) / 550 * (x1 - x0)
        text(c, (x, y + 64), str(v), 30, MUTED, "Medium", "ma", al)
    mx = x0 + (marker - 300) / 550 * (x1 - x0)
    c.d.polygon([(mx - 22, y - 46), (mx + 22, y - 46), (mx, y - 8)], fill=fade(INK, al))
    text(c, (mx, y - 60), str(int(marker)), 54, INK, "Bold", "ms", al, disp=True)
    if label: text(c, (960, y + 150), label, 34, MUTED, "Medium", "ma", al)

def donut(c, cx, cy, R, parts, prog, al, hi=None):
    start = -90.0; total = sum(p for p, _ in parts)
    for i, (p, lab) in enumerate(parts):
        sweep = 360 * p / total
        show = clamp(prog * len(parts) - i)
        if show <= 0: break
        col = SEG[i]
        if hi is not None and i not in hi: col = mix(col, BG, .7)
        c.d.pieslice((cx - R, cy - R, cx + R, cy + R), start, start + sweep * show, fill=fade(col, al))
        start += sweep
    c.d.ellipse((cx - R * .58, cy - R * .58, cx + R * .58, cy + R * .58), fill=BG)

# ---------- биты ----------
def b_title(c, p):
    al = c.a()
    if p.get("kicker"): text(c, (960, 330), p["kicker"].upper(), 34, ACC, "Bold", "ma", c.a(0))
    lines = wrap(p["text"], 92, 1500, "Bold")
    for i, ln in enumerate(lines): text(c, (960, 400 + i * 108), ln, 92, INK, "Bold", "ma", c.a(.1 + .1 * i), disp=True)
    if p.get("sub"): text(c, (960, 430 + len(lines) * 108), p["sub"], 40, MUTED, "Medium", "ma", c.a(.5))

def b_section(c, p):
    text(c, (960, 300), p["n"], 34, ACC, "Bold", "ma", c.a())
    text(c, (960, 360), p["text"], 100, INK, "Bold", "ma", c.a(.1), disp=True)
    al = c.a(.35, .6)
    w = 360 * al
    rrect(c, (960 - w / 2, 540, 960 + w / 2, 700), 40, ACC, al)
    if al > .4: text(c, (960, 620), p["pct"], 110, CARD, "Bold", "mm", clamp((al - .4) / .6), disp=True)
    text(c, (960, 760), "of your FICO Score", 36, MUTED, "Medium", "ma", c.a(.7))

def b_people(c, p):
    for i, x in enumerate((640, 1280)):
        al = c.a(.15 * i); person(c, x, 500, 1.5, INK if i == 0 else BLUE, al)
        rrect(c, (x - 170, 640, x + 170, 720), 20, CARD, al, LINE, 2)
        text(c, (x, 680), "$60,000 / yr", 40, INK, "Bold", "mm", al)
    text(c, (960, 120), "Same salary. Same mortgage.", 56, INK, "Bold", "ma", c.a(.3), disp=True)
    if p.get("result"):
        for i, (x, ok, lab) in enumerate(((640, True, "Lower rate"), (1280, False, "Higher rate / denied"))):
            al = c.a(.2 + .5 * i); check(c, x + 120, 360, 52, al, ok)
            text(c, (x, 760), lab, 44, GREEN if ok else RED, "Bold", "ma", al)
    text(c, (960, 850), "Example for illustration", 26, MUTED, "Medium", "ma", c.a(.5))

def b_gauge(c, p):
    text(c, (960, 220), p.get("head", "Your credit score"), 60, INK, "Bold", "ma", c.a(), disp=True)
    lo, hi = p.get("sweep", (430, 780))
    m = lo + (hi - lo) * (0.5 - 0.5 * math.cos(min(c.lt / 3.0, 1) * math.pi)) if c.lt < 3 else hi + 25 * math.sin((c.lt - 3) * .8)
    gauge(c, 560, c.a(.1), m, p.get("label"))

def b_disclaimer(c, p):
    al = c.a(); off = card(c, (460, 360, 1460, 720), al)
    text(c, (960, 430 + off), "EDUCATION ONLY", 40, ACC, "Bold", "ma", al)
    text(c, (960, 500 + off), "Not financial advice.", 72, INK, "Bold", "ma", c.a(.15), disp=True)
    text(c, (960, 610 + off), "Your situation may be different.", 40, MUTED, "Medium", "ma", c.a(.3))

def b_flow(c, p):
    al0, al1, al2 = c.a(), c.a(.4), c.a(.8)
    for (x, lab, col, al) in ((520, "You", INK, al0), (1400, "Lender", ACC, al1)):
        off = card(c, (x - 220, 380, x + 220, 640), al)
        person(c, x, 520 + off, .9, col, al) if lab == "You" else None
        if lab == "Lender":
            for k in range(4): c.d.rectangle((x - 110 + k * 60, 440 + off, x - 80 + k * 60, 560 + off), fill=fade(ACC, al))
            c.d.polygon([(x - 140, 440 + off), (x + 140, 440 + off), (x, 390 + off)], fill=fade(ACC, al))
        text(c, (x, 590 + off), lab, 40, INK, "Bold", "ma", al)
    w = 520 * al2
    c.d.line([(720, 510), (720 + w, 510)], fill=fade(INK, al2), width=8)
    if al2 > .9: c.d.polygon([(1240, 490), (1240, 530), (1270, 510)], fill=INK)
    text(c, (960, 230), "Will you pay it back?", 70, INK, "Bold", "ma", c.a(.9), disp=True)
    text(c, (960, 760), "Approval  ·  Interest rate", 44, ACC, "Bold", "ma", c.a(1.6))

def b_bureaus(c, p):
    text(c, (960, 220), "Built from your credit reports", 60, INK, "Bold", "ma", c.a(), disp=True)
    for i, name in enumerate(("Equifax", "Experian", "TransUnion")):
        x = 460 + i * 500; al = c.a(.3 + .25 * i); off = card(c, (x - 200, 400, x + 200, 700), al)
        for k in range(4): rrect(c, (x - 140, 470 + off + k * 40, x + (140 if k else 40), 488 + off + k * 40), 8, SOFT, al)
        text(c, (x, 650 + off), name, 44, INK, "Bold", "mm", al)
    text(c, (960, 800), "The 3 major credit bureaus", 36, MUTED, "Medium", "ma", c.a(1.2))

def b_two_apps(c, p):
    text(c, (960, 200), "You don't have just one score", 60, INK, "Bold", "ma", c.a(), disp=True)
    for i, (x, v, lab) in enumerate(((700, 742, "App A"), (1220, 718, "Lender sees"))):
        al = c.a(.3 + .3 * i); off = card(c, (x - 170, 320, x + 170, 840), al, 44)
        text(c, (x, 400 + off), lab, 34, MUTED, "Medium", "ma", al)
        text(c, (x, 560 + off), str(v), 120, INK, "Bold", "mm", al, disp=True)
        text(c, (x, 680 + off), "FICO 8" if i == 0 else "another version", 30, ACC, "Bold", "ma", al)
    text(c, (960, 870), "Example numbers  ·  FICO versions, VantageScore", 28, MUTED, "Medium", "ma", c.a(1))

FACT = [(35, "Payment history"), (30, "Amounts owed"), (15, "Length of history"), (10, "New credit"), (10, "Credit mix")]
def b_donut(c, p):
    F = [tuple(x) for x in p["parts"]] if "parts" in p else FACT
    hi = p.get("hi"); prog = clamp(c.lt / p.get("build", 9.0)) if not hi else 1
    donut(c, 620, 540, 320, F, prog, c.a(), hi)
    text(c, (960, 140), p.get("head", "What's in your FICO Score"), 60, INK, "Bold", "ma", c.a(), disp=True)
    for i, (pct, lab) in enumerate(F):
        show = clamp(prog * len(F) - i) if not hi else 1
        if show <= 0: continue
        al = ease(show) * (1 if (hi is None or i in hi) else .35)
        y = 330 + i * 110
        rrect(c, (1080, y, 1124, y + 44), 10, SEG[i], al)
        text(c, (1150, y + 22), lab, 46, INK, "SemiBold", "lm", al)
        text(c, (1720, y + 22), f"{pct}%", 50, INK, "Bold", "rm", al, disp=True)
    if hi: text(c, (620, 540), "65%", 96, INK, "Bold", "mm", c.a(.3), disp=True)
    text(c, (620, 920), p.get("src", "Source: myFICO"), 24, MUTED, "Medium", "ma", c.a(1))

def b_calendar(c, p):
    text(c, (960, 180), "Do you pay on time?", 64, INK, "Bold", "ma", c.a(), disp=True)
    months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    for i, m in enumerate(months):
        r, k = divmod(i, 6); x = 330 + k * 220; y = 330 + r * 260; al = c.a(.08 * i, .3)
        late = (i == 8)
        rrect(c, (x, y, x + 180, y + 200), 26, (255, 236, 234) if late else CARD, al, RED if late else LINE, 3)
        text(c, (x + 90, y + 40), m, 32, MUTED, "Medium", "ma", al)
        if late: text(c, (x + 90, y + 140), "LATE", 40, RED, "Bold", "mm", c.a(1.4))
        else: check(c, x + 90, y + 130, 38, al, True)

def b_timeline(c, p):
    text(c, (960, 200), "How long negatives can stay on your report", 54, INK, "Bold", "ma", c.a(), disp=True)
    rows = [("Late payment", 7, GOLD, "up to 7 years"), ("Chapter 7 bankruptcy", 10, RED, "up to 10 years")]
    for i, (lab, yrs, col, s) in enumerate(rows):
        y = 420 + i * 220; al = c.a(.3 + .6 * i); w = 1000 * yrs / 10 * ease((c.lt - .3 - .6 * i) / 1.2)
        text(c, (300, y - 50), lab, 42, INK, "SemiBold", "la", al)
        rrect(c, (300, y + 10, 1300, y + 80), 20, SOFT, al)
        if w > 40: rrect(c, (300, y + 10, 300 + w, y + 80), 20, col, al)
        text(c, (1340, y + 45), s, 44, col, "Bold", "lm", al)
    text(c, (960, 850), "Source: CFPB (most negative info: 7 years)", 26, MUTED, "Medium", "ma", c.a(1.2))

def b_toggle(c, p):
    text(c, (960, 260), "Never miss a payment", 70, INK, "Bold", "ma", c.a(), disp=True)
    on = ease((c.lt - .8) / .4); al = c.a(.2)
    off = card(c, (560, 420, 1360, 700), al, 40)
    text(c, (640, 560 + off), "Autopay (minimum)", 50, INK, "Bold", "lm", al)
    tx = 1140; rrect(c, (tx, 520 + off, tx + 160, 600 + off), 40, mix(LINE, GREEN, on), al)
    kx = tx + 40 + 80 * on; c.d.ellipse((kx - 32, 528 + off, kx + 32, 592 + off), fill=fade(CARD, al))
    text(c, (960, 800), "Your safety net — pay more by hand anytime", 40, MUTED, "Medium", "ma", c.a(1.2))

def b_util(c, p):
    lim, bal = p["limit"], p["balance"]
    text(c, (960, 170), "Credit utilization", 64, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.2); off = card(c, (300, 300, 1620, 560), al, 36)
    text(c, (360, 350 + off), p.get("label", "Card limit"), 36, MUTED, "Medium", "la", al)
    text(c, (1560, 350 + off), f"${lim:,}", 44, INK, "Bold", "ra", al)
    rrect(c, (360, 430 + off, 1560, 500 + off), 22, SOFT, al)
    f = bal / lim * ease((c.lt - .8) / 1.2)
    if f > .02: rrect(c, (360, 430 + off, 360 + 1200 * f, 500 + off), 22, GOLD if bal / lim >= .3 else GREEN, al)
    text(c, (360, 520 + off), f"Balance ${bal:,}", 34, INK, "SemiBold", "la", c.a(1))
    a2 = c.a(2.0)
    text(c, (960, 700), f"${bal:,}  ÷  ${lim:,}  =  {round(bal / lim * 100)}%", 92, INK, "Bold", "ma", a2, disp=True)
    text(c, (960, 840), "Lower is generally better", 40, MUTED, "Medium", "ma", c.a(3))

def b_bignum(c, p):
    text(c, (960, 240), p["head"], 56, INK, "Bold", "ma", c.a(), disp=True)
    text(c, (960, 520), p["num"], 260, ACC, "Bold", "mm", c.a(.3), disp=True)
    for i, ln in enumerate(wrap(p["sub"], 44, 1300, "Medium")):
        text(c, (960, 720 + i * 60), ln, 44, INK, "Medium", "ma", c.a(.6))
    if p.get("src"): text(c, (960, 860), p["src"], 26, MUTED, "Medium", "ma", c.a(1))

def b_statement(c, p):
    text(c, (960, 180), "Timing matters", 64, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.2); y = 560
    c.d.line([(260, y), (1660, y)], fill=fade(INK, al), width=6)
    for i in range(31):
        x = 260 + i * 1400 / 30; c.d.line([(x, y - 14), (x, y + 14)], fill=fade(MUTED, al), width=3)
    sx = 260 + 20 * 1400 / 30; px = 260 + 14 * 1400 / 30
    a1 = c.a(.8); rrect(c, (sx - 150, y - 210, sx + 150, y - 110), 24, INK, a1)
    text(c, (sx, y - 160), "Statement date", 36, CARD, "Bold", "mm", a1)
    c.d.line([(sx, y - 110), (sx, y - 16)], fill=fade(INK, a1), width=5)
    a2 = c.a(2.2); rrect(c, (px - 170, y + 80, px + 170, y + 180), 24, GREEN, a2)
    text(c, (px, y + 130), "Pay part here", 38, CARD, "Bold", "mm", a2)
    c.d.line([(px, y + 16), (px, y + 80)], fill=fade(GREEN, a2), width=5)
    text(c, (960, 840), "The reported balance is often your statement balance", 36, MUTED, "Medium", "ma", c.a(1.4))

def b_recover(c, p):
    text(c, (960, 170), "Utilization has no long memory", 60, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.2); x0, x1, y0, y1 = 300, 1620, 320, 820
    c.d.line([(x0, y1), (x1, y1)], fill=fade(LINE, al), width=4)
    pts = []
    for i in range(61):
        t = i / 60; v = 0.75 - 0.35 * math.exp(-((t - .4) / .1) ** 2) if t < .4 else 0.4 + 0.37 * (1 - math.exp(-(t - .4) * 9))
        if t < .4: v = 0.75 - 0.35 * (t / .4) ** 3
        pts.append((x0 + t * (x1 - x0), y1 - v * (y1 - y0)))
    n = int(len(pts) * clamp(c.lt / 3.0))
    if n > 1: c.d.line(pts[:n], fill=fade(ACC, al), width=10, joint="curve")
    text(c, (x0 + .42 * (x1 - x0), y1 - .3 * (y1 - y0)), "high balance reported", 32, RED, "Bold", "ma", c.a(1.3))
    text(c, (x0 + .8 * (x1 - x0), y1 - .85 * (y1 - y0)), "paid down → recovers", 32, GREEN, "Bold", "ma", c.a(2.4))
    text(c, (960, 860), "Illustration, not real data", 26, MUTED, "Medium", "ma", c.a(1))

def b_accounts(c, p):
    text(c, (960, 180), "How long your accounts have been open", 58, INK, "Bold", "ma", c.a(), disp=True)
    rows = [("Oldest card", 12), ("Car loan", 5), ("Newest card", 1)]
    for i, (lab, yrs) in enumerate(rows):
        y = 360 + i * 150; al = c.a(.3 + .3 * i); w = 1000 * yrs / 12 * ease((c.lt - .3 - .3 * i) / 1)
        text(c, (300, y + 35), lab, 40, INK, "SemiBold", "lm", al)
        if w > 30: rrect(c, (620, y, 620 + w, y + 70), 20, SEG[i], al)
        text(c, (640 + w, y + 35), f"{yrs} yr" + ("s" if yrs > 1 else ""), 38, INK, "Bold", "lm", al)
    text(c, (960, 840), "Average age: 6 years  ·  example", 40, MUTED, "Medium", "ma", c.a(1.5))

def b_keepcard(c, p):
    text(c, (960, 200), "Think twice before closing an old card", 60, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.2)
    rrect(c, (660, 330, 1260, 700), 36, INK, al)
    rrect(c, (720, 420, 820, 490), 12, GOLD, al)
    text(c, (720, 600), "•••• 2014", 44, CARD, "Bold", "la", al)
    text(c, (1200, 370), "NO FEE", 30, GOLD, "Bold", "ra", al)
    a2 = c.a(1.2)
    rrect(c, (560, 760, 1360, 860), 30, GREEN, a2)
    text(c, (960, 810), "Holds up your history + total limit", 40, CARD, "Bold", "mm", a2)

def b_inquiry(c, p):
    text(c, (960, 170), "Hard inquiry", 64, INK, "Bold", "ma", c.a(), disp=True)
    text(c, (960, 260), "A lender checks your credit when you apply", 38, MUTED, "Medium", "ma", c.a(.2))
    rows = [("Stays on your report", "about 2 years", 1.0, MUTED), ("FICO counts it", "past 12 months", .5, ACC)]
    for i, (lab, s, f, col) in enumerate(rows):
        y = 420 + i * 200; al = c.a(.6 + .7 * i); w = 1100 * f * ease((c.lt - .6 - .7 * i) / 1)
        text(c, (360, y - 40), lab, 40, INK, "SemiBold", "la", al)
        rrect(c, (360, y + 20, 1460, y + 90), 20, SOFT, al)
        if w > 30: rrect(c, (360, y + 20, 360 + w, y + 90), 20, col, al)
        text(c, (1500, y + 55), s, 40, col if col != MUTED else INK, "Bold", "lm", al)
    text(c, (960, 850), "One inquiry: usually a small effect  ·  many at once can add up", 34, MUTED, "Medium", "ma", c.a(2))

def b_soft(c, p):
    al = c.a(); off = card(c, (660, 200, 1260, 820), al, 60)
    text(c, (960, 380 + off), "Your score", 40, MUTED, "Medium", "ma", al)
    text(c, (960, 520 + off), "742", 160, INK, "Bold", "mm", al, disp=True)
    a2 = c.a(.8); rrect(c, (720, 660 + off, 1200, 760 + off), 30, GREEN, a2)
    text(c, (960, 710 + off), "Soft inquiry: no impact", 38, CARD, "Bold", "mm", a2)
    text(c, (960, 880), "Check as often as you like", 44, INK, "Bold", "ma", c.a(1.2))

def b_mix(c, p):
    text(c, (960, 200), "Different types of credit", 64, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.3); rrect(c, (420, 380, 820, 640), 30, INK, al); rrect(c, (470, 440, 550, 495), 10, GOLD, al)
    text(c, (620, 700), "Credit card", 42, INK, "Bold", "ma", al)
    al2 = c.a(.7)
    rrect(c, (1100, 470, 1500, 590), 40, BLUE, al2); rrect(c, (1180, 400, 1420, 490), 40, BLUE, al2)
    for x in (1180, 1420): c.d.ellipse((x - 45, 545, x + 45, 635), fill=fade(INK, al2))
    text(c, (1300, 700), "Installment loan", 42, INK, "Bold", "ma", al2)
    a3 = c.a(1.6); rrect(c, (640, 790, 1280, 870), 30, MUTED, a3)
    text(c, (960, 830), "Smallest factor: 10%", 42, CARD, "Bold", "mm", a3)

def b_myth(c, p):
    text(c, (960, 120), f"MYTH #{p['n']}", 40, RED, "Bold", "ma", c.a())
    al = c.a(.15); lines = wrap("“" + p["myth"] + "”", 60, 1150, "Bold")
    off = card(c, (310, 200, 1610, 260 + 76 * len(lines) + 40), al, 36)
    k = c.a(1.0, .5)
    for i, ln in enumerate(lines):
        y = 260 + off + i * 76
        text(c, (960, y), ln, 60, INK, "Bold", "mm", al, disp=True)
        lw = F(60, "Bold", True).getlength(ln)
        if k > 0: c.d.line([(960 - lw / 2 - 10, y + 2), (960 - lw / 2 - 10 + (lw + 20) * k, y + 2)], fill=RED, width=9)
    a2 = c.a(1.6); flines = wrap(p["fact"], 52, 1150, "SemiBold"); top = 260 + 76 * len(lines) + 110
    off2 = card(c, (310, top, 1610, top + 100 + 66 * len(flines)), a2, 36)
    text(c, (380, top + 30 + off2), "FACT", 34, GREEN, "Bold", "la", a2)
    for i, ln in enumerate(flines):
        text(c, (380, top + 80 + off2 + i * 66), ln, 52, INK, "SemiBold", "la", a2)
    if p.get("src"): text(c, (960, 860), p["src"], 26, MUTED, "Medium", "ma", c.a(2))

def b_reveal(c, p):
    for i, x in enumerate((640, 1280)):
        person(c, x, 420, 1.3, INK if i == 0 else BLUE, c.a(.1 * i))
    text(c, (960, 160), "Same salary. Different rates. Why?", 56, INK, "Bold", "ma", c.a(), disp=True)
    for i, s in enumerate(("Payment history", "Balances", "Time")):
        x = 460 + i * 500; al = c.a(1.0 + .5 * i)
        rrect(c, (x - 210, 640, x + 210, 740), 30, SEG[i], al)
        text(c, (x, 690), s, 44, CARD, "Bold", "mm", al)
    text(c, (960, 800), "Not income", 54, RED, "Bold", "ma", c.a(2.6), disp=True)

def b_browser(c, p):
    text(c, (960, 160), "Get your free credit reports", 62, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.2); off = card(c, (360, 260, 1560, 820), al, 24)
    c.d.rectangle((362, 262 + off, 1558, 340 + off), fill=fade(SOFT, al))
    for k, col in enumerate((RED, GOLD, GREEN)): c.d.ellipse((400 + k * 40, 288 + off, 424 + k * 40, 312 + off), fill=fade(col, al))
    rrect(c, (560, 280 + off, 1500, 322 + off), 20, CARD, al)
    text(c, (590, 301 + off), "annualcreditreport.com", 30, INK, "Medium", "lm", c.a(.5))
    for i, s in enumerate(("Free  ·  weekly", "All 3 bureaus", "Official site (US)")):
        a = c.a(1 + .4 * i); check(c, 520, 450 + off + i * 110, 30, a, True)
        text(c, (580, 450 + off + i * 110), s, 46, INK, "SemiBold", "lm", a)
    text(c, (960, 860), "Reports don't include your score  ·  Source: FTC", 30, MUTED, "Medium", "ma", c.a(1.8))

def b_errors(c, p):
    text(c, (960, 160), "Look for mistakes", 62, INK, "Bold", "ma", c.a(), disp=True)
    rows = ["Card ••4410   Open   $0", "Auto loan   Paid as agreed", "Card ••9921   30 days late", "Store card   Open   $120"]
    al = c.a(.2); off = card(c, (360, 260, 1560, 780), al, 24)
    for i, r in enumerate(rows):
        y = 320 + off + i * 110; bad = (i == 2); a = c.a(.3 + .15 * i)
        hl = c.a(1.4)
        if bad: rrect(c, (390, y - 10, 1530, y + 80), 16, (255, 236, 234), hl)
        text(c, (430, y + 35), r, 42, RED if bad and hl > .5 else INK, "SemiBold", "lm", a)
        if bad: text(c, (1500, y + 35), "Error?  →  Dispute", 38, RED, "Bold", "rm", hl)
    text(c, (960, 850), "Errors can be fixed  ·  accurate negatives can't be removed early", 32, MUTED, "Medium", "ma", c.a(2))

def b_checklist(c, p):
    text(c, (960, 140), p.get("head", "This week"), 62, INK, "Bold", "ma", c.a(), disp=True)
    items = p["items"]; step = p.get("step", 1.6)
    for i, s in enumerate(items):
        y = 250 + i * 118; a = c.a(p["tm"][i] if "tm" in p else i * step)
        check(c, 520, y + 40, 34, a, True)
        text(c, (590, y + 40), s, 50, INK, "SemiBold", "lm", a)

def b_subscribe(c, p):
    text(c, (960, 180), "Next video", 40, ACC, "Bold", "ma", c.a())
    al = c.a(.2); off = card(c, (460, 260, 1460, 640), al, 36)
    for i, ln in enumerate(wrap(p.get("next", "How credit card interest really works"), 70, 860, "Bold")):
        text(c, (960, 330 + off + i * 86), ln, 70, INK, "Bold", "ma", al, disp=True)
    text(c, (960, 560 + off), p.get("next_sub", "+ why the minimum payment is a trap"), 40, MUTED, "Medium", "ma", al)
    a2 = c.a(1.2); pulse = 1 + .04 * math.sin(c.lt * 4) * (a2 >= 1)
    w = 260 * pulse; rrect(c, (960 - w, 740, 960 + w, 850), 55, RED, a2)
    text(c, (960, 795), "SUBSCRIBE", 54, CARD, "Bold", "mm", a2)


# ---------- биты с персонажем и для темы «проценты по картам» ----------
def b_say(c, p):
    al = c.a(.3); x0, y0, x1 = 820, 260, 1700
    lines = wrap(p["text"], 58, x1 - x0 - 120, "Bold")
    subl = wrap(p["sub"], 38, x1 - x0 - 120, "Bold") if p.get("sub") else []
    y1 = y0 + 90 + len(lines) * 74 + len(subl) * 52 + (14 if subl else 0)
    off = card(c, (x0, y0, x1, y1), al, 40)
    c.d.polygon([(x0 + 2, y0 + 150 + off), (x0 - 70, y0 + 200 + off), (x0 + 2, y0 + 210 + off)], fill=fade(CARD, al))
    for i, ln in enumerate(lines): text(c, (x0 + 60, y0 + 50 + off + i * 74), ln, 58, INK, "Bold", "la", al, disp=True)
    for i, ln in enumerate(subl): text(c, (x0 + 60, y0 + 64 + off + len(lines) * 74 + i * 52), ln, 38, ACC, "Bold", "la", c.a(.8))

def b_debtcard(c, p):
    al = c.a(.2); rrect(c, (820, 300, 1560, 740), 44, INK, al)
    rrect(c, (900, 400, 1010, 480), 14, GOLD, al)
    text(c, (900, 560), "Balance", 36, (170, 180, 200), "Medium", "la", al)
    text(c, (900, 600), p.get("bal", "$5,000"), 96, CARD, "Bold", "la", c.a(.4), disp=True)
    text(c, (1480, 400), p.get("apr", "22% APR"), 44, GOLD, "Bold", "ra", c.a(.7))
    text(c, (1190, 800), p.get("sub", "Paying only the minimum"), 44, INK, "Bold", "ma", c.a(1.2))

def b_lines(c, p):
    text(c, (960, 150), p["head"], 60, INK, "Bold", "ma", c.a(), disp=True)
    y = 300; step = p.get("step", 1.2)
    for i, ln in enumerate(p["lines"]):
        ln = ln if isinstance(ln, list) else [ln]
        s = ln[0]; size = next((x for x in ln[1:] if isinstance(x, int)), 64); col = INK
        text(c, (960, y), s, size, col, "Bold", "ma", c.a(.3 + i * step), disp=True)
        y += size + 54
    if p.get("note"): text(c, (960, 860), p["note"], 30, MUTED, "Medium", "ma", c.a(1))

def b_compound(c, p):
    text(c, (960, 150), "Interest on interest", 62, INK, "Bold", "ma", c.a(), disp=True)
    n = 8; base = 1.0; x0 = 360; bw = 120; y1 = 800
    for i in range(n):
        a = c.a(.3 + i * .35, .4)
        if a <= 0: break
        tot = base * (1.12 ** i); h0 = 300 * base; h1 = 300 * tot
        x = x0 + i * 160
        rrect(c, (x, y1 - h0 * a, x + bw, y1), 10, BLUE, a)
        if i: c.d.rectangle((x, y1 - h1 * a, x + bw, y1 - h0 * a + 10), fill=fade(RED, a))
    rrect(c, (380, 860, 420, 890), 8, BLUE, c.a(1)); text(c, (440, 875), "what you borrowed", 32, INK, "Medium", "lm", c.a(1))
    rrect(c, (900, 860, 940, 890), 8, RED, c.a(1)); text(c, (960, 875), "interest added to the balance", 32, INK, "Medium", "lm", c.a(1))
    text(c, (1700, 150), "illustration", 26, MUTED, "Medium", "ra", c.a(1))

def b_grace(c, p):
    text(c, (960, 150), "The grace period", 64, INK, "Bold", "ma", c.a(), disp=True)
    y = 470; al = c.a(.3)
    w1 = 820 * ease((c.lt - .3) / 1.2); rrect(c, (240, y, 240 + w1, y + 90), 24, BLUE, al)
    text(c, (650, y + 45), "Billing cycle (~1 month)", 38, CARD, "Bold", "mm", c.a(1.2))
    a2 = c.a(1.6); w2 = 520 * ease((c.lt - 1.6) / 1)
    if w2 > 20: rrect(c, (1080, y, 1080 + w2, y + 90), 24, GREEN, a2)
    text(c, (1340, y + 45), "Grace period", 38, CARD, "Bold", "mm", c.a(2.4))
    for x, lab, a in ((1070, "Statement closes", c.a(1.4)), (1610, "Due date", c.a(2.4))):
        c.d.line([(x, y - 40), (x, y + 130)], fill=fade(INK, a), width=5)
        text(c, (x, y - 90), lab, 34, INK, "Bold", "ma", a)
    a3 = c.a(3.2); rrect(c, (300, 700, 1620, 800), 30, GREEN, a3)
    text(c, (960, 750), "Statement balance paid in full = $0 interest on purchases", 40, CARD, "Bold", "mm", a3)
    text(c, (960, 860), "On most cards  ·  Source: CFPB", 28, MUTED, "Medium", "ma", c.a(3.6))

def b_atm(c, p):
    text(c, (960, 150), "Cash advance", 64, INK, "Bold", "ma", c.a(), disp=True)
    al = c.a(.3); rrect(c, (300, 280, 760, 800), 30, (70, 80, 100), al)
    rrect(c, (350, 330, 710, 520), 16, (150, 210, 200), al)
    text(c, (530, 425), "$ $ $", 64, INK, "Bold", "mm", al)
    for r in range(3):
        for q in range(3): rrect(c, (380 + q * 110, 560 + r * 70, 460 + q * 110, 610 + r * 70), 10, (200, 205, 215), al)
    for i, s in enumerate(("Usually no grace period", "Interest can start the same day", "Often a higher rate + a fee")):
        a = c.a(1 + i * 1.2); check(c, 900, 380 + i * 150, 34, a, False)
        text(c, (960, 380 + i * 150), s, 48, INK, "SemiBold", "lm", a)

STMT = [("Statement balance", "$1,240.18"), ("Current balance", "$1,385.42"), ("Minimum payment due", "$37.00"),
        ("Payment due date", "Dec 18"), ("Interest charged", "$21.64")]
def b_statement5(c, p):
    text(c, (960, 120), "Find these 5 numbers", 60, INK, "Bold", "ma", 1, disp=True)
    hi = p.get("hi", -1); off = card(c, (420, 220, 1500, 840), 1, 28)
    for i, (lab, val) in enumerate(STMT):
        y = 270 + i * 110
        on = i == hi
        if on: rrect(c, (450, y, 1470, y + 90), 18, (226, 244, 236), c.a(0, .3))
        col = ACC if on else (INK if i <= hi else MUTED)
        text(c, (490, y + 45), f"{i + 1}. {lab}", 44, col, "Bold" if on else "SemiBold", "lm", 1)
        text(c, (1430, y + 45), val, 44, col, "Bold", "rm", 1)
    text(c, (960, 870), "Example statement", 28, MUTED, "Medium", "ma", 1)

def b_minsplit(c, p):
    text(c, (960, 150), "Your first minimum payment: $141.67", 58, INK, "Bold", "ma", c.a(), disp=True)
    x0, x1, y = 260, 1660, 420; tot = 141.67; f = 91.67 / tot
    a = c.a(.5); xi = x0 + (x1 - x0) * f * ease((c.lt - .5) / 1)
    rrect(c, (x0, y, x1, y + 140), 30, SOFT, a)
    if xi > x0 + 20: rrect(c, (x0, y, xi, y + 140), 30, RED, a)
    a2 = c.a(1.8)
    if a2 > 0: rrect(c, (x0 + (x1 - x0) * f + 6, y, x1, y + 140), 30, GREEN, a2)
    text(c, (x0 + (x1 - x0) * f / 2, y + 70), "Interest  $91.67", 46, CARD, "Bold", "mm", c.a(1.3))
    text(c, (x0 + (x1 - x0) * (1 + f) / 2, y + 70), "Debt  $50", 46, CARD, "Bold", "mm", a2)
    text(c, (960, 680), "$5,000 at 22% APR  ·  minimum = 1% of balance + interest", 38, MUTED, "Medium", "ma", c.a(2.4))
    text(c, (960, 860), "Example  ·  formulas differ by bank and country", 28, MUTED, "Medium", "ma", c.a(2.6))

PAY = [("Minimum only", 230, "19 years", "$8,100", RED), ("Fixed $150 / month", 52, "52 months", "$2,800", GOLD),
       ("Fixed $200 / month", 34, "34 months", "$1,750", GREEN)]
def b_payoff(c, p):
    text(c, (960, 130), "Same $5,000. Same 22% APR.", 58, INK, "Bold", "ma", c.a() if p["stage"] == 1 else 1, disp=True)
    text(c, (1640, 230), "Interest paid", 34, MUTED, "Bold", "ra", 1)
    for i, (lab, m, tl, intr, col) in enumerate(PAY[:p["stage"]]):
        new = i == p["stage"] - 1; a = c.a(.2) if new else 1
        y = 290 + i * 180; w = 1000 * m / 230 * (ease((c.lt - .2) / 1.4) if new else 1)
        text(c, (260, y), lab, 40, INK, "SemiBold", "la", a)
        if w > 30: rrect(c, (260, y + 55, 260 + w, y + 125), 20, col, a)
        text(c, (280 + w, y + 90), tl, 40, col, "Bold", "lm", a)
        text(c, (1640, y + 90), intr, 56, col, "Bold", "rm", a, disp=True)
    text(c, (960, 860), "Simplified example: no new purchases or fees", 28, MUTED, "Medium", "ma", 1)


# ---------- общие биты: рост, столбики, страны ----------
def b_growth(c, p):
    text(c, (960, 120), p.get("head", "$200 a month at 7% a year"), 58, INK, "Bold", "ma", c.a(), disp=True)
    x0, x1, y0, y1 = 300, 1620, 230, 780; maxv = p.get("max", 540000)
    al = c.a(.2); c.d.line([(x0, y1), (x1, y1)], fill=fade(LINE, al), width=4)
    for k, lab in ((0, "25"), (0.25, "35"), (0.5, "45"), (0.75, "55"), (1, "65")):
        text(c, (x0 + k * (x1 - x0), y1 + 20), lab, 30, MUTED, "Medium", "ma", al)
    text(c, (x1, y1 + 60), "age", 28, MUTED, "Medium", "ra", al)
    amt = p.get("monthly", 200)
    for ln in p["lines"]:
        start, col, delay = ln[0], tuple(ln[1]), ln[2]; stop = ln[3] if len(ln) > 3 else 65
        pts = []; b = 0.0
        for m in range(480):
            b = b * (1 + .07 / 12) + (amt if (start - 25) * 12 <= m < (stop - 25) * 12 else 0)
            if m % 6 == 0: pts.append((x0 + m / 480 * (x1 - x0), y1 - b / maxv * (y1 - y0)))
        n = int(len(pts) * clamp((c.lt - delay) / 3.0))
        if n > 1: c.d.line(pts[:n], fill=col, width=9, joint="curve")
        if n == len(pts):
            lab = (f"invest {start}–{stop} only" if stop < 65 else f"start at {start}") + f": ~${round(b / 1000)}k"
            if start > 25: text(c, (x0 + 20, y0 + 40), lab, 38, col, "Bold", "la", 1)
            else: text(c, (x1 - 10, pts[-1][1] - 50), lab, 38, col, "Bold", "ra", 1)
    if p.get("contrib"):
        a = c.a(p["contrib"]); y = y1 - p.get("contrib_v", 96000) / maxv * (y1 - y0)
        c.d.line([(x0, y), (x1, y)], fill=fade(MUTED, a), width=3)
        text(c, (x0 + 10, y - 44), p.get("contrib_lab", "you put in $96k"), 32, MUTED, "Bold", "la", a)
    text(c, (960, 870), "Example, not a promise: returns vary and can be negative", 28, MUTED, "Medium", "ma", c.a(1))

def b_bars(c, p):
    text(c, (960, 130), p["head"], 58, INK, "Bold", "ma", c.a(), disp=True)
    mx = p.get("max") or max(r[1] for r in p["rows"]); sh = p.get("shown", 0)
    if len(p["rows"]) > 4 or p.get("compact"):  # компактный режим: подпись слева, полоса справа
        for i, (lab, v, disp, col) in enumerate(p["rows"]):
            dl = 0 if i < sh else .3 + (i - sh) * p.get("step", 1.0)
            lw = p.get("lw", 260); bx = 300 + lw
            y = 250 + i * 100; a = 1.0 if i < sh else c.a(dl); w = (1160 - lw) * v / mx * (1 if i < sh else ease((c.lt - dl) / 1.2))
            text(c, (300, y + 40), lab, 40, INK, "SemiBold", "lm", a)
            if w > 30: rrect(c, (bx, y + 10, bx + w, y + 70), 18, tuple(col), a)
            text(c, (bx + 20 + w, y + 40), disp, 42, tuple(col), "Bold", "lm", a, disp=True)
        if p.get("note"): text(c, (960, 870), p["note"], 28, MUTED, "Medium", "ma", c.a(1))
        return
    for i, (lab, v, disp, col) in enumerate(p["rows"]):
        dl = 0 if i < sh else .3 + (i - sh) * p.get("step", 1.0)
        y = 290 + i * 190; a = 1.0 if i < sh else c.a(dl); w = 1050 * v / mx * (1 if i < sh else ease((c.lt - dl) / 1.2))
        text(c, (300, y), lab, 42, INK, "SemiBold", "la", a)
        if w > 30: rrect(c, (300, y + 60, 300 + w, y + 140), 22, tuple(col), a)
        text(c, (320 + w, y + 100), disp, 46, tuple(col), "Bold", "lm", a, disp=True)
    if p.get("note"): text(c, (960, 870), p["note"], 28, MUTED, "Medium", "ma", c.a(1))

def b_countries(c, p):
    text(c, (960, 110), p.get("head", "Tax-advantaged accounts"), 58, INK, "Bold", "ma", c.a(), disp=True)
    rows = p.get("rows") or [("United States", "401(k)  ·  IRA"), ("United Kingdom", "Stocks & Shares ISA  ·  pension"),
            ("Canada", "TFSA  ·  RRSP"), ("Australia", "Superannuation")]
    for i, (cn, acc) in enumerate(rows):
        y = 210 + i * 150; a = c.a(p["tm"][i] if "tm" in p else i)
        off = card(c, (300, y, 1620, y + 120), a, 26)
        text(c, (350, y + 60 + off), cn, 46, INK, "Bold", "lm", a)
        text(c, (1580, y + 60 + off), acc, 42, ACC, "Bold", "rm", a)
    text(c, (960, 840), "Rules and limits change: check your government's official website", 30, MUTED, "Medium", "ma", c.a(4))

def b_twocol(c, p):
    text(c, (960, 130), p["head"], 58, INK, "Bold", "ma", c.a(), disp=True)
    for i, (title, items, col) in enumerate(p["cols"]):
        x = 300 + i * 680; a = c.a(.4 + i * p.get("step", 1.5)); off = card(c, (x, 250, x + 640, 800), a, 34)
        rrect(c, (x, 250 + off, x + 640, 350 + off), 34, tuple(col), a); c.d.rectangle((x, 310 + off, x + 640, 350 + off), fill=fade(tuple(col), a))
        text(c, (x + 320, 300 + off), title, 48, CARD, "Bold", "mm", a)
        yy = 420
        for s in items:
            for j, ln in enumerate(wrap(s, 40, 540, "SemiBold")):
                text(c, (x + 50, yy + off), ("• " if j == 0 else "   ") + ln, 40, INK, "SemiBold", "la", a); yy += 54
            yy += 26


def b_pricepath(c, p):
    text(c, (960, 120), p["head"], 58, INK, "Bold", "ma", c.a(), disp=True)
    pts = p["points"]; mx = p.get("max", max(v for _, v, _ in pts) * 1.1)
    x0, x1, y0, y1 = 300, 1620, 240, 800
    al = c.a(.2); c.d.line([(x0, y1), (x1, y1)], fill=fade(LINE, al), width=4)
    xy = [(x0 + (x1 - x0) * i / (len(pts) - 1), y1 - v / mx * (y1 - y0)) for i, (_, v, _) in enumerate(pts)]
    for i, ((lab, v, col), (x, y)) in enumerate(zip(pts, xy)):
        tm = p["tm"][i] if "tm" in p else i * 1.5
        a = c.a(tm)
        if i and a > 0:
            px, py = xy[i - 1]; c.d.line([(px, py), (px + (x - px) * a, py + (y - py) * a)], fill=tuple(col), width=9)
        if a > 0:
            c.d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=fade(tuple(col), a))
            text(c, (x, y - 40), lab, 40, tuple(col), "Bold", "ms", a)
    if p.get("note"): text(c, (960, 860), p["note"], 28, MUTED, "Medium", "ma", c.a(1))

def b_lifeline(c, p):
    text(c, (960, 120), p.get("head", "Warren Buffett's early years"), 58, INK, "Bold", "ma", 1, disp=True)
    ev = p["events"]; x0, x1, y = 260, 1660, 520
    c.d.line([(x0, y), (x1, y)], fill=LINE, width=8)
    for i, (age, lab) in enumerate(ev):
        tm = p["tm"][i] if "tm" in p else i * 1.5
        a = c.a(tm); x = x0 + (x1 - x0) * i / (len(ev) - 1)
        on = i == len([1 for t_ in (p.get("tm") or []) if c.lt >= t_]) - 1
        col = ACC if on else INK
        c.d.ellipse((x - 26, y - 26, x + 26, y + 26), fill=fade(col, a))
        text(c, (x, y - 50), f"age {age}", 40, col, "Bold", "ms", a, disp=True)
        for k, ln in enumerate(wrap(lab, 32, 250, "SemiBold")): text(c, (x, y + 60 + k * 42), ln, 32, INK, "SemiBold", "ma", a)

def b_hook(c, p):
    """Крючок первых секунд: рубрика + крупное обещание/боль, слова появляются быстро."""
    text(c, (960, 250), p.get("kicker", "").upper(), 34, ACC, "Bold", "ma", c.a(0, .25))
    words = p["text"].split(); lines = wrap(p["text"], 84, 1560, "Bold")
    shown = int(len(words) * clamp(c.lt / p.get("reveal", 1.6))) + 1; k = 0
    y = 520 - len(lines) * 52
    for ln in lines:
        lw = ln.split(); vis = " ".join(lw[:max(0, shown - k)]); k += len(lw)
        if vis: text(c, (960, y), vis, 84, INK, "Bold", "ma", 1, disp=True)
        y += 104
    bw = 700 * ease((c.lt - .3) / .8); c.d.rounded_rectangle((960 - bw / 2, y + 20, 960 + bw / 2, y + 32), 6, fill=ACC)

def b_ident(c, p):
    """Заставка рубрики: цветная плашка на весь кадр, название рубрики и ролика."""
    a = ease(c.lt / .35); x = W * (1 - a)
    c.d.rectangle((x, 0, W, H), fill=ACC)
    c.d.rectangle((x, H - 120, W, H), fill=PILL)
    if a > .6:
        al = ease((c.lt - .25) / .3)
        text(c, (x + 960, 380), p.get("series", "").upper(), 40, mix(ACC, CARD, al), "Bold", "ma")
        for i, ln in enumerate(wrap(p["title"], 96, 1600, "Bold")):
            text(c, (x + 960, 460 + i * 112), ln, 96, mix(ACC, CARD, al), "Bold", "ma", disp=True)

def b_score(c, p):
    """Карточка участника сравнения: имя + шкалы 1–5 (рейтинг) с подписями."""
    al = c.a(); col = tuple(p.get("color", ACC))
    off = card(c, (360, 150, 1560, 830), al, 34)
    c.d.rounded_rectangle((360, 150 + off, 1560, 270 + off), 34, fill=fade(col, al)); c.d.rectangle((360, 230 + off, 1560, 270 + off), fill=fade(col, al))
    text(c, (420, 210 + off), p.get("tag", ""), 34, CARD, "Bold", "lm", al)
    text(c, (1500, 210 + off), p["name"], 52, CARD, "Bold", "rm", al, disp=True)
    for i, (lab, n, note) in enumerate(p["rows"]):
        y = 340 + i * 150 + off; a = c.a(.4 + i * p.get("step", 1.2))
        text(c, (430, y + 30), lab, 44, INK, "Bold", "lm", a)
        for j in range(5):
            on = j < n; x = 760 + j * 76
            c.d.rounded_rectangle((x, y + 8, x + 60, y + 52), 12, fill=fade(col if on else LINE, a))
        text(c, (1160, y + 30), note, 34, MUTED, "SemiBold", "lm", a)

def b_question(c, p):
    """Карточка вопроса: большой номер в круге + текст вопроса (формат Q&A)."""
    al = c.a(); cx, cy = 560, 470
    r = 150 * (.85 + .15 * ease(c.lt / .5))
    c.d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=fade(ACC, al))
    text(c, (cx, cy), p.get("tag", "Q"), 130, CARD, "Bold", "mm", al, disp=True)
    lines = wrap(p["q"], 64, 860, "Bold")
    y = 470 - len(lines) * 40
    for i, ln in enumerate(lines): text(c, (800, y + i * 80), ln, 64, INK, "Bold", "la", c.a(.25), disp=True)
    if p.get("sub"): text(c, (800, y + len(lines) * 80 + 20), p["sub"], 38, MUTED, "Medium", "la", c.a(.6))

def b_takeaway(c, p):
    """Финальная мысль одной фразой (вместо списка Recap)."""
    lines = wrap(p["text"], 72, 1500, "Bold")
    y = 430 - len(lines) * 46
    text(c, (960, y - 90), p.get("head", "The one thing to remember"), 36, ACC, "Bold", "ma", c.a())
    for i, ln in enumerate(lines): text(c, (960, y + i * 92), ln, 72, INK, "Bold", "ma", c.a(.3 + i * .15), disp=True)

BEATS = {k[2:]: v for k, v in globals().items() if k.startswith("b_")}

# ---------- субтитры / тайминг ----------
def sub_chunks(txt):
    out = []
    for s in re.split(r"(?<=[.?!])\s+", txt.strip()):
        while len(s) > 72:
            cut = max(s.rfind(", ", 0, 72), s.rfind(" — ", 0, 72), s.rfind(": ", 0, 72))
            if cut < 25: cut = s.rfind(" ", 0, 72)
            out.append(s[:cut + 1].strip()); s = s[cut + 1:].strip()
        if s: out.append(s)
    return out

def build_timeline(ep, audio_dir):
    t, secs = 0.0, []
    for i, sec in enumerate(ep.SECTIONS):
        import glob
        f = sorted(glob.glob(os.path.join(audio_dir, f"s{i:02d}.*")))[0]
        d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
        txt = sec["text"]; L = len(txt)
        beats = []
        for b in sec["beats"]:
            key = b["at"]; pos = 0 if key == "^" else txt.find(key)
            if pos < 0: raise SystemExit(f"key not found in section {i}: {key}")
            bt = t + d * pos / L
            if "marks" in b:
                b = dict(b); b["tm"] = []
                for mk in b["marks"]:
                    mp = txt.find(mk)
                    if mp < 0: raise SystemExit(f"mark not found in section {i}: {mk}")
                    b["tm"].append(t + d * mp / L - bt)
            beats.append((bt, b))
        subs, cpos = [], 0
        for ch in sub_chunks(txt):
            p = txt.find(ch, cpos); cpos = p + len(ch)
            subs.append((t + d * p / L, t + d * cpos / L + .15, ch))
        secs.append({"start": t, "dur": d, "file": f, "beats": beats, "subs": subs, "label": sec["label"]})
        t += d + GAP
    return secs, t

def render_frame(secs, total, T):
    img = Image.new("RGB", (W, H), BG)
    draw_motif(ImageDraw.Draw(img))
    sec = secs[0]
    for s in secs:
        if T >= s["start"] - .01: sec = s
    beat_t, beat = sec["beats"][0]
    for bt, b in sec["beats"]:
        if T >= bt - .05: beat_t, beat = bt, b
    nxt = [bt for bt, _ in sec["beats"] if bt > beat_t] + [sec["start"] + sec["dur"] + GAP]
    c = Ctx(img, T - beat_t, nxt[0] - beat_t)
    BEATS[beat["type"]](c, beat)
    if beat.get("char"):
        ch = beat["char"]; pose, cx, hh = ch[0], ch[1], ch[2]; look = ch[3] if len(ch) > 3 else None
        al = c.a(0, .5); blink = (T % 3.7) < .13
        character.paste(img, pose, cx, 900 + (1 - al) * 400, hh, blink, 4 * math.sin(T * 2.2), look)
    d = c.d
    # шапка (не на крючке и заставке)
    if beat["type"] not in ("hook", "ident"): d.rounded_rectangle((60, 46, 60 + F(26, "Bold").getlength(sec["label"].upper()) + 48, 96), 25, fill=PILL)
    if beat["type"] not in ("hook", "ident"): d.text((84, 71), sec["label"].upper(), font=F(26, "Bold"), fill=CARD, anchor="lm")
    # прогресс
    d.rectangle((0, H - 8, W, H), fill=LINE); d.rectangle((0, H - 8, W * T / total, H), fill=ACC)
    # субтитр
    cur = [s for s in sec["subs"] if s[0] <= T < s[1]]
    if cur:
        s = cur[-1][2]; lines = wrap(s, 38, 1740, "SemiBold")
        h = 54 * len(lines) + 26; y0 = H - 36 - h
        wmax = max(F(38, "SemiBold").getlength(l) for l in lines)
        d.rounded_rectangle((960 - wmax / 2 - 30, y0, 960 + wmax / 2 + 30, y0 + h), 22, fill=(20, 33, 61))
        for i, ln in enumerate(lines):
            d.text((960, y0 + 13 + 27 + i * 54), ln, font=F(38, "SemiBold"), fill=CARD, anchor="mm")
    return img

def render_chunk(args):
    ep_path, audio_dir, i0, i1, out = args
    ep = load(ep_path); secs, total = build_timeline(ep, audio_dir)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                          "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for f in range(i0, i1):
        p.stdin.write(render_frame(secs, total, f / FPS).tobytes())
    p.stdin.close(); p.wait()
    return out

def load(path):
    spec = importlib.util.spec_from_file_location("ep", path); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m); apply_theme(getattr(m, "THEME", None))
    character.DEFAULT_LOOK = getattr(m, "LOOK", "finn"); return m

def main(ep_path, audio_dir, out, stills=None):
    ep = load(ep_path); secs, total = build_timeline(ep, audio_dir)
    work = os.path.join(os.path.dirname(out), "work"); os.makedirs(work, exist_ok=True)
    if stills:
        for T in stills:
            render_frame(secs, total, T).save(os.path.join(work, f"still_{T:06.1f}.png"))
        print("stills done"); return
    n = int(total * FPS); k = 4; step = math.ceil(n / k)
    jobs = [(ep_path, audio_dir, j * step, min(n, (j + 1) * step), os.path.join(work, f"part{j}.mp4")) for j in range(k)]
    with Pool(k) as pool: parts = pool.map(render_chunk, jobs)
    with open(os.path.join(work, "parts.txt"), "w") as fh:
        for pth in parts: fh.write(f"file '{pth}'\n")
    # голос: разделы с паузами
    inputs, flt = [], []
    for i, s in enumerate(secs):
        inputs += ["-i", s["file"]]
        flt.append(f"[{i}:a]aresample=44100,adelay={int(s['start'] * 1000)}|{int(s['start'] * 1000)}[a{i}]")
    flt.append("".join(f"[a{i}]" for i in range(len(secs))) + f"amix=inputs={len(secs)}:normalize=0,acompressor=threshold=-22dB:ratio=3:attack=5:release=120:makeup=2,alimiter=limit=0.7[out]")
    voice0 = os.path.join(work, "voice0.wav"); voice = os.path.join(work, "voice.wav")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(flt),
                           "-map", "[out]", "-t", f"{total:.2f}", "-ar", "48000", voice0])
    meas = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", voice0, "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                           "-f", "null", "-"], capture_output=True, text=True).stderr
    m = json.loads(meas[meas.rfind("{"):meas.rfind("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-i", voice0, "-af", ln, "-ar", "48000", voice])
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(work, "parts.txt"),
                           "-i", voice, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", out])
    print("done", out, f"{total:.1f}s")

if __name__ == "__main__":
    a = sys.argv[1:]
    stills = [float(x) for x in a[3].split(",")] if len(a) > 3 else None
    main(a[0], a[1], a[2], stills)

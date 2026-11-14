"""Движок объясняющих роликов 16:9 (1920x1080) для финансового канала без лица.
Голос: по одному mp3 на раздел сценария. Визуал: Pillow (схемы, шкалы, диаграммы), субтитры, прогресс.
Синхронизация: каждый «бит» сцены привязан к ключевой фразе текста раздела; время = доля символов * длительность.
Запуск: python3 explainer.py <episode.py> <audio_dir> <out.mp4>
"""
import json, math, os, re, subprocess, sys, importlib.util
from multiprocessing import Pool
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1920, 1080, 25
GAP = 0.7  # пауза между разделами, с
FONT_DIR = "/usr/share/fonts/opentype/inter/"

BG = (247, 244, 238); INK = (20, 33, 61); MUTED = (112, 120, 138); LINE = (226, 220, 208)
CARD = (255, 255, 255); ACC = (16, 122, 96); GOLD = (222, 160, 36); RED = (206, 64, 60)
GREEN = (36, 156, 92); BLUE = (52, 104, 214); SOFT = (236, 231, 221)
SEG = [ACC, BLUE, GOLD, (140, 100, 200), (232, 120, 80)]

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
    hi = p.get("hi"); prog = clamp(c.lt / p.get("build", 9.0)) if not hi else 1
    donut(c, 620, 540, 320, FACT, prog, c.a(), hi)
    text(c, (960, 140), p.get("head", "What's in your FICO Score"), 60, INK, "Bold", "ma", c.a(), disp=True)
    for i, (pct, lab) in enumerate(FACT):
        show = clamp(prog * len(FACT) - i) if not hi else 1
        if show <= 0: continue
        al = ease(show) * (1 if (hi is None or i in hi) else .35)
        y = 330 + i * 110
        rrect(c, (1080, y, 1124, y + 44), 10, SEG[i], al)
        text(c, (1150, y + 22), lab, 46, INK, "SemiBold", "lm", al)
        text(c, (1720, y + 22), f"{pct}%", 50, INK, "Bold", "rm", al, disp=True)
    if hi: text(c, (620, 540), "65%", 96, INK, "Bold", "mm", c.a(.3), disp=True)
    text(c, (620, 920), "Source: myFICO", 24, MUTED, "Medium", "ma", c.a(1))

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
        y = 250 + i * 118; a = c.a(i * step)
        check(c, 520, y + 40, 34, a, True)
        text(c, (590, y + 40), s, 50, INK, "SemiBold", "lm", a)

def b_subscribe(c, p):
    text(c, (960, 180), "Next video", 40, ACC, "Bold", "ma", c.a())
    al = c.a(.2); off = card(c, (460, 260, 1460, 640), al, 36)
    for i, ln in enumerate(wrap("How credit card interest really works", 70, 860, "Bold")):
        text(c, (960, 330 + off + i * 86), ln, 70, INK, "Bold", "ma", al, disp=True)
    text(c, (960, 560 + off), "+ why the minimum payment is a trap", 40, MUTED, "Medium", "ma", al)
    a2 = c.a(1.2); pulse = 1 + .04 * math.sin(c.lt * 4) * (a2 >= 1)
    w = 260 * pulse; rrect(c, (960 - w, 740, 960 + w, 850), 55, RED, a2)
    text(c, (960, 795), "SUBSCRIBE", 54, CARD, "Bold", "mm", a2)

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
        f = os.path.join(audio_dir, f"s{i:02d}.mp3")
        d = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
        txt = sec["text"]; L = len(txt)
        beats = []
        for b in sec["beats"]:
            key = b["at"]; pos = 0 if key == "^" else txt.find(key)
            if pos < 0: raise SystemExit(f"key not found in section {i}: {key}")
            beats.append((t + d * pos / L, b))
        subs, cpos = [], 0
        for ch in sub_chunks(txt):
            p = txt.find(ch, cpos); cpos = p + len(ch)
            subs.append((t + d * p / L, t + d * cpos / L + .15, ch))
        secs.append({"start": t, "dur": d, "file": f, "beats": beats, "subs": subs, "label": sec["label"]})
        t += d + GAP
    return secs, t

def render_frame(secs, total, T):
    img = Image.new("RGB", (W, H), BG)
    sec = secs[0]
    for s in secs:
        if T >= s["start"] - .01: sec = s
    beat_t, beat = sec["beats"][0]
    for bt, b in sec["beats"]:
        if T >= bt - .05: beat_t, beat = bt, b
    nxt = [bt for bt, _ in sec["beats"] if bt > beat_t] + [sec["start"] + sec["dur"] + GAP]
    c = Ctx(img, T - beat_t, nxt[0] - beat_t)
    BEATS[beat["type"]](c, beat)
    d = c.d
    # шапка
    d.rounded_rectangle((60, 46, 60 + F(26, "Bold").getlength(sec["label"].upper()) + 48, 96), 25, fill=INK)
    d.text((84, 71), sec["label"].upper(), font=F(26, "Bold"), fill=CARD, anchor="lm")
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
    spec.loader.exec_module(m); return m

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
    flt.append("".join(f"[a{i}]" for i in range(len(secs))) + f"amix=inputs={len(secs)}:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[out]")
    voice = os.path.join(work, "voice.wav")
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", *inputs, "-filter_complex", ";".join(flt),
                           "-map", "[out]", "-t", f"{total:.2f}", "-ar", "48000", voice])
    subprocess.check_call(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", os.path.join(work, "parts.txt"),
                           "-i", voice, "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", out])
    print("done", out, f"{total:.1f}s")

if __name__ == "__main__":
    a = sys.argv[1:]
    stills = [float(x) for x in a[3].split(",")] if len(a) > 3 else None
    main(a[0], a[1], a[2], stills)

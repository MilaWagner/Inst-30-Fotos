"""Персонаж канала «Finn» — взрослый мужчина ~35–40 лет, 2D, рисуется кодом (бесплатно, всегда одинаковый).
Пиджак, рубашка, галстук, очки, аккуратная стрижка с проседью на висках.
Позы: idle, wave, point_right, point_left, think, happy, worried, shrug, thumbs_up.
draw(pose, height, blink=False) -> RGBA Image (якорь: низ-центр, между ступнями).
"""
from PIL import Image, ImageDraw, ImageFilter

INK = (22, 24, 32)
# Образы: Finn (утверждённый, в трёх нарядах) и второстепенные герои. draw(..., look="maya") и т.п.
LOOKS = {
    "finn":        dict(skin=(238, 196, 160), skin_d=(214, 166, 130), hair=(52, 44, 40), temples=(150, 146, 142), style="short", glasses=True,
                        outfit="suit", top=(34, 52, 92), top_d=(26, 40, 72), shirt=(236, 240, 246), tie=(16, 122, 96), legs=(44, 50, 62), shoe=(30, 24, 22)),
    "finn_casual": dict(skin=(238, 196, 160), skin_d=(214, 166, 130), hair=(52, 44, 40), temples=(150, 146, 142), style="short", glasses=True,
                        outfit="sweater", top=(150, 54, 60), top_d=(118, 40, 46), shirt=(236, 240, 246), legs=(58, 72, 104), shoe=(70, 50, 36)),
    "finn_hoodie": dict(skin=(238, 196, 160), skin_d=(214, 166, 130), hair=(52, 44, 40), temples=(150, 146, 142), style="short", glasses=True,
                        outfit="hoodie", top=(70, 110, 90), top_d=(52, 86, 70), shirt=(236, 240, 246), legs=(50, 56, 70), shoe=(240, 240, 240)),
    "maya":        dict(skin=(176, 120, 86), skin_d=(150, 98, 68), hair=(34, 24, 20), style="long", glasses=False, lips=(170, 70, 80),
                        outfit="blazer", top=(196, 82, 58), top_d=(160, 62, 44), shirt=(250, 244, 236), legs=(40, 44, 56), shoe=(40, 30, 30)),
    "sam":         dict(skin=(205, 150, 112), skin_d=(180, 128, 92), hair=(30, 22, 18), style="curly", glasses=False,
                        outfit="hoodie", top=(240, 170, 40), top_d=(205, 140, 30), shirt=(250, 250, 250), legs=(46, 70, 120), shoe=(245, 245, 245)),
    "rose":        dict(skin=(242, 206, 178), skin_d=(220, 178, 148), hair=(196, 196, 200), style="bob", glasses=True, lips=(190, 90, 100),
                        outfit="sweater", top=(112, 78, 160), top_d=(88, 60, 130), shirt=(250, 250, 250), legs=(70, 70, 84), shoe=(60, 40, 40)),
}
DEFAULT_LOOK = "finn"

# координаты: (0,0) — пол между ступнями, вверх — минус.
SH_L, SH_R = (-82, -452), (82, -452)
REST_L = ((-104, -350), (-110, -250)); REST_R = ((104, -350), (110, -250))
POSES = {
    "idle":        dict(l=REST_L, r=REST_R, face="smile"),
    "wave":        dict(l=REST_L, r=((160, -490), (175, -590)), face="open"),
    "point_right": dict(l=REST_L, r=((180, -450), (280, -455)), face="smile", finger="r"),
    "point_left":  dict(l=((-180, -450), (-280, -455)), r=REST_R, face="smile", finger="l"),
    "think":       dict(l=((-100, -360), (-15, -380)), r=((100, -360), (35, -495)), face="think"),
    "happy":       dict(l=((-150, -520), (-165, -620)), r=((150, -520), (165, -620)), face="open"),
    "worried":     dict(l=((-108, -390), (-58, -515)), r=((108, -390), (58, -515)), face="worried"),
    "shrug":       dict(l=((-150, -415), (-205, -470)), r=((150, -415), (205, -470)), face="flat"),
    "thumbs_up":   dict(l=REST_L, r=((165, -400), (185, -490)), face="smile", thumb="r"),
}
SS = 2
_cache = {}

def draw(pose="idle", height=600, blink=False, look=None):
    look = look or DEFAULT_LOOK
    key = (pose, height, blink, look)
    if key in _cache: return _cache[key]
    p = POSES[pose]; L = LOOKS[look]
    SKIN, SKIN_D, HAIR = L["skin"], L["skin_d"], L["hair"]
    JACKET, JACKET_D, SHIRT, PANTS, SHOE = L["top"], L["top_d"], L["shirt"], L["legs"], L["shoe"]
    outfit, style = L["outfit"], L["style"]
    k = height / 700 * SS
    W, H = int(720 * k), int(760 * k)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    ox, oy = W / 2, H - 30 * k
    P = lambda x, y: (ox + x * k, oy + y * k)
    def circ(x, y, r, fill): cx, cy = P(x, y); d.ellipse((cx - r * k, cy - r * k, cx + r * k, cy + r * k), fill=fill)
    def limb(a, b, w, col):
        d.line([P(*a), P(*b)], fill=col, width=int(w * k)); circ(*a, w / 2, col); circ(*b, w / 2, col)

    for s in (-1, 1):
        limb((s * 34, -235), (s * 40, -22), 44, PANTS)
        cx, cy = P(s * 50, -14); d.ellipse((cx - 42 * k, cy - 17 * k, cx + 42 * k, cy + 17 * k), fill=SHOE)
    if outfit == "hoodie":  # капюшон за шеей
        d.ellipse((*P(-78, -540), *P(78, -440)), fill=JACKET_D)
    if style in ("long", "bob"):  # волосы за головой
        if style == "long": d.rounded_rectangle((*P(-96, -655), *P(96, -395)), int(46 * k), fill=HAIR)
        else: d.rounded_rectangle((*P(-80, -655), *P(80, -540)), int(40 * k), fill=HAIR)
    d.rounded_rectangle((*P(-86, -475), *P(86, -215)), int(34 * k), fill=JACKET)
    if outfit in ("suit", "blazer"):
        d.polygon([P(-30, -475), P(30, -475), P(0, -395)], fill=SHIRT if outfit == "suit" else SKIN)
        if outfit == "suit" and L.get("tie"):
            d.polygon([P(-9, -462), P(9, -462), P(13, -400), P(0, -385), P(-13, -400)], fill=L["tie"])
        if outfit == "blazer":
            for xx in (-14, 0, 14): circ(xx, -440 + abs(xx) * -0.6, 4, (240, 220, 150))
        d.line([P(-30, -475), P(-6, -360)], fill=JACKET_D, width=int(6 * k))
        d.line([P(30, -475), P(6, -360)], fill=JACKET_D, width=int(6 * k))
        for yb in (-330, -290): circ(0, yb, 5, JACKET_D)
    elif outfit == "sweater":
        d.chord((*P(-34, -490), *P(34, -450)), 0, 180, fill=SHIRT)
        d.rounded_rectangle((*P(-86, -240), *P(86, -215)), int(10 * k), fill=JACKET_D)
    elif outfit == "hoodie":
        d.line([P(-14, -465), P(-16, -410)], fill=SHIRT, width=int(5 * k)); d.line([P(14, -465), P(16, -410)], fill=SHIRT, width=int(5 * k))
        d.rounded_rectangle((*P(-58, -320), *P(58, -255)), int(18 * k), fill=JACKET_D)
    for side, sh in (("l", SH_L), ("r", SH_R)):
        el, hd = p[side]
        limb(sh, el, 36, JACKET)
        limb(el, hd, 32, JACKET)
        circ(*hd, 23, SKIN)
        if p.get("finger") == side:
            dx = 1 if side == "r" else -1
            limb(hd, (hd[0] + 44 * dx, hd[1] - 4), 16, SKIN)
        if p.get("thumb") == side:
            limb(hd, (hd[0] - 4, hd[1] - 44), 16, SKIN)
    limb((0, -475), (0, -505), 30, SKIN)
    d.ellipse((*P(-66, -640), *P(66, -480)), fill=SKIN)
    circ(-66, -560, 13, SKIN_D); circ(66, -560, 13, SKIN_D)
    if style == "short":
        d.chord((*P(-70, -652), *P(70, -540)), 180, 360, fill=HAIR)
        d.ellipse((*P(-70, -652), *P(36, -598)), fill=HAIR)
        if L.get("temples"):
            for s in (-1, 1): d.rectangle((*P(s * 70 - (8 if s > 0 else 0), -598), *P(s * 70 + (0 if s > 0 else 8), -575)), fill=L["temples"])
    elif style == "curly":
        for cx_, cy_, r_ in ((-52, -612, 26), (-22, -634, 28), (12, -638, 28), (44, -622, 27), (62, -596, 20), (-64, -590, 20)): circ(cx_, cy_, r_, HAIR)
    elif style in ("long", "bob"):
        d.chord((*P(-72, -655), *P(72, -548)), 180, 360, fill=HAIR)
        d.pieslice((*P(-72, -655), *P(40, -585)), 90, 270, fill=HAIR)
    face = p["face"]; ey = -566
    for s in (-1, 1):
        ex = s * 27
        if blink: d.line([P(ex - 10, ey), P(ex + 10, ey)], fill=INK, width=int(5 * k))
        else: circ(ex, ey, 6.5, INK)
        if L.get("glasses"): d.rounded_rectangle((*P(ex - 19, ey - 14), *P(ex + 19, ey + 14)), int(7 * k), outline=INK, width=int(4 * k))
        by = ey - 26
        if face == "worried": d.line([P(ex - 15, by + (0 if s < 0 else -7)), P(ex + 15, by + (-7 if s < 0 else 0))], fill=HAIR, width=int(6 * k))
        elif face == "think": d.line([P(ex - 15, by - (6 if s > 0 else 0)), P(ex + 15, by - (6 if s > 0 else 0))], fill=HAIR, width=int(6 * k))
        else: d.line([P(ex - 15, by + 1), P(ex + 15, by - 1)], fill=HAIR, width=int(6 * k))
    if L.get("glasses"): d.line([P(-8, ey), P(8, ey)], fill=INK, width=int(4 * k))
    d.line([P(0, -556), P(-5, -532), P(3, -530)], fill=SKIN_D, width=int(4 * k))
    my = -510
    lipc = L.get("lips", INK)
    if face == "smile": d.arc((*P(-22, my - 18), *P(22, my + 8)), 20, 160, fill=lipc, width=int(5 * k))
    elif face == "open":
        d.chord((*P(-22, my - 12), *P(22, my + 16)), 0, 180, fill=INK)
        d.chord((*P(-12, my + 4), *P(12, my + 15)), 0, 180, fill=(210, 90, 90))
    elif face == "worried": d.arc((*P(-16, my - 2), *P(16, my + 16)), 200, 340, fill=INK, width=int(5 * k))
    elif face == "think": d.line([P(-12, my + 4), P(16, my)], fill=INK, width=int(5 * k))
    else: d.line([P(-14, my + 3), P(14, my + 3)], fill=INK, width=int(5 * k))
    a = im.getchannel("A").filter(ImageFilter.MaxFilter(7))
    ol = Image.new("RGBA", im.size, INK + (0,)); ol.putalpha(a); ol.alpha_composite(im)
    out = ol.resize((W // SS, H // SS), Image.LANCZOS)
    _cache[key] = out
    return out

def paste(base, pose, cx, bottom, height=600, blink=False, bob=0.0, look=None):
    im = draw(pose, height, blink, look)
    base.paste(im, (int(cx - im.width / 2), int(bottom - im.height + bob)), im)

if __name__ == "__main__":
    import sys
    sheet = Image.new("RGB", (1920, 1080), (247, 244, 238)); dd = ImageDraw.Draw(sheet)
    poses = ["idle", "wave", "point_right", "think", "happy", "thumbs_up"]
    for i, lk in enumerate(LOOKS):
        cx = 170 + i * 315
        paste(sheet, poses[i % len(poses)], cx, 520, 440, look=lk); dd.text((cx, 40), lk, fill=(20, 33, 61), anchor="ma")
        paste(sheet, "worried" if i % 2 else "shrug", cx, 1060, 440, look=lk)
    sheet.save(sys.argv[1] if len(sys.argv) > 1 else "character_sheet.png")

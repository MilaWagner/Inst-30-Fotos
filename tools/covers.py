"""Обложки 9:16 для 7 роликов (в сетке профиля TikTok показывается центральная часть 3:4)."""
import sys
sys.path.insert(0, "/home/user/Inst-30-Fotos/tools")
from PIL import Image, ImageDraw
from slide_engine import W, H, BG, INK, ITAL, HB, HI, text_w, photo_layer, avatar, put, HANDLE

OUT = "/home/user/Inst-30-Fotos/videos/"
# (фон, строки заголовка [(текст, курсив?)], фото)
COVERS = {
1: ("brown", [[("Свобода — ", 0)], [("это не сказка", 1)]], 3),
2: ("cream", [[("Мама ", 0), ("троих", 1)], [("и онлайн", 0)]], 1),
3: ("brown", [[("Зачем женщине", 0)], [("свой доход", 1), ("?", 0)]], 5),
4: ("cream", [[("Нужен ли", 0)], [("свой курс", 1), ("?", 0)]], 2),
5: ("brown", [[("Жить так, ", 0)], [("как удобно тебе", 1)]], 3),
6: ("cream", [[("Из офлайна", 0)], [("в онлайн", 1)]], 1),
7: ("brown", [[("Ты ", 0), ("не опоздала", 1)]], 2),
}

def cover(n):
    bg, lines, pid = COVERS[n]
    f = Image.new("RGBA", (W, H), BG[bg] + (255,))
    f.alpha_composite(avatar(), (88, 300))
    ImageDraw.Draw(f).text((200, 348), HANDLE, font=HB(40), fill=INK, anchor="lm")
    size0 = 128; y = 600
    for line in lines:
        size = size0
        tot = sum(text_w(t, HI(size) if it else HB(size)) for t, it in line)
        if tot > 904: size = int(size * 904 / tot)
        x = 88
        d = ImageDraw.Draw(f)
        for txt, it in line:
            fnt = HI(size) if it else HB(size)
            d.text((x, y), txt, font=fnt, fill=ITAL[bg] if it else INK, anchor="ls"); x += text_w(txt, fnt)
        y += int(size0 * 1.15)
    ph = photo_layer(pid, 640, 780)
    put(f, ph, 540, 1230, 1.0, angle=-3 if n % 2 else 3)
    im = f.convert("RGB")
    im.save(OUT + f"cover_{n}.png"); im.save(OUT + f"cover_{n}.jpg", quality=92)

if __name__ == "__main__":
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else range(1, 8)):
        cover(n); print("cover", n)

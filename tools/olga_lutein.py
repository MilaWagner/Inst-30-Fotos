"""Ольга (FitLine), ролик «Для глаз» (microSolve⁺ Lutein) в её стиле.
Голос: её запись (audio/lutein_voice.wav, если есть) или бесплатный Vosk TTS.
Запуск: python3 -I olga_lutein.py [prev|all]"""
import sys, os
sys.path.insert(0, "/home/user/Inst-30-Fotos/tools")
from PIL import Image, ImageDraw
import olga_magnij as O
E = O.E

SP, OUT = O.SP, O.OUT
O.VOICE_REC = SP + "audio/lutein_voice.wav"
O.PRODUCT_PHOTO = SP + "product_lutein.png"

# Текст субтитров (нормальное написание: 24, B2, FitLine)
TEXT = ("Отодвигаешь телефон подальше… чтобы прочитать сообщение? Буквы расплываются, да? "
        "Меню в ресторане — без очков уже не прочитать. Даже в тарелку смотришь… и без очков не видишь, что там. "
        "А к вечеру — всё как в тумане. Знакомо? "
        "После сорока с этим сталкиваются очень многие. Глазам нужна поддержка. Каждый день. "
        "Витамин B2 способствует поддержанию нормального зрения. "
        "А в немецком продукте FitLine microSolve+ Lutein — лютеин и витамин B2. "
        "Всего 24 капли — в стакан воды. Один раз в день. "
        "Хочешь попробовать? Напиши мне слово ХОЧУ — и я пришлю ссылку!")

H = lambda *l: [list(x) for x in l]
B, C = "brown", "cream"
SCENES = [
 dict(sents=(0, 2), bg=B, head=H([("Телефон ", 0), ("подальше?", 1)]),
      els=[{"k": "clip", "seq": [("43270", 3.8, 0.5), ("13810", 99, -3.0)], "y": 1010, "w": 760, "h": 620, "ang": -2}]),
 dict(sents=(2, 4), bg=C, head=H([("Без очков — ", 0)], [("не прочитать", 1)]),
      els=[{"k": "clip", "seq": [("12873", 3.2, 2.0), ("14727", 99, -1.0)], "y": 1030, "ang": 2}]),
 dict(sents=(4, 6), bg=B, head=H([("Всё как ", 0), ("в тумане", 1)]),
      els=[{"k": "clip", "seq": [("41180", 99, 1.0)], "y": 1010, "ang": -2}]),
 dict(sents=(6, 9), bg=C, head=H([("После ", 0), ("сорока", 1)]),
      els=[{"k": "pills", "items": ["у очень многих", "поддержка каждый день"], "x": 540, "y": 670, "step": 130, "size": 46, "at": 0.05, "gap": 1.2},
           {"k": "clip", "seq": [("14710", 99, 1.0)], "y": 1170, "h": 420, "ang": 2}]),
 dict(sents=(9, 10), bg=B, head=H([("Витамин ", 0), ("B2", 1)]), hsize=120,
      els=[{"k": "cards2", "a": ("B2", "витамин"), "b": ("зрение", "нормальное"), "y": 860, "at": 0.1}]),
 dict(sents=(10, 11), bg=C, head=H([("Немецкий ", 0), ("продукт", 1)]),
      els=[{"k": "jar", "x": 540, "y": 1040, "s": 1.2, "ang": 3, "at": 0.05}]),
 dict(sents=(11, 13), bg=B, head=H([("Как ", 0), ("пить", 1)]),
      els=[{"k": "pills", "items": ["24 капли", "в стакан воды", "1 раз в день"], "x": 300, "y": 720, "step": 150, "size": 48, "at": 0.0, "gap": 0.5},
           {"k": "clip", "seq": [("47955", 99, 1.5)], "x": 760, "y": 1120, "w": 420, "h": 560, "ang": 3}]),
 dict(sents=(13, 15), bg=C, head=H([("Напиши ", 0), ("ХОЧУ", 1)]),
      els=[{"k": "msg", "word": "ХОЧУ", "y": 780, "at": 0.15}, {"k": "jar", "x": 540, "y": 1190, "s": 0.95, "ang": -3, "at": 0.6}]),
]

# Текст для озвучки: ударения «+», паузы «...»/«-», латиница кириллицей, цифры словами
TEXT_VOICE = ("Отодвигаешь телефон подальше... чтобы прочитать сообщение? Буквы расплываются, да? "
        "Меню в ресторане - без очков уже не прочитать. Даже в тарелку смотришь... и без очков не видишь, что там. "
        "А к вечеру - всё как в тумане. Знакомо? "
        "После сорока с этим сталкиваются очень многие. Глазам нужна поддержка. Каждый день. "
        "Витамин бэ два способствует поддержанию нормального зрения. "
        "А в немецком продукте Фитлайн Микросолв плюс Лютеин - лютеин и витамин бэ два. "
        "Всего двадцать четыре капли - в стакан воды. Один раз в день. "
        "Хочешь попробовать? Напиши мне слово хочу! И я пришлю ссылку.")

def make():
    return O.OlgaVideo(0, TEXT, O.narration("olga_lutein", TEXT_VOICE), SCENES, OUT + "olga_lutein.mp4")

def cover(path_png):
    if O.DECOR is None: O.DECOR = O._decor()
    f = Image.new("RGBA", (E.W, E.H), E.BG["cream"] + (255,))
    f.alpha_composite(E.avatar(), (88, 300))
    ImageDraw.Draw(f).text((200, 348), E.HANDLE, font=E.HB(40), fill=E.INK, anchor="lm")
    y = 560
    for line in [[("Без очков ", 0)], [("не видишь ", 0), ("текст?", 1)]]:
        x = 88; d = ImageDraw.Draw(f)
        for txt, it in line:
            fnt = E.HI(124) if it else E.HB(124)
            d.text((x, y), txt, font=fnt, fill=E.ITAL["cream"] if it else E.INK, anchor="ls"); x += E.text_w(txt, fnt)
        y += 145
    E.put(f, O.clip_layer("13810", 3.0, 600, 620), 400, 1060, 1.0, angle=-3)
    E.put(f, O.jar_layer(0.0), 820, 1250, 0.6, angle=6)
    E.put(f, E.pill_layer("для глаз", 54, E.CARD_DARK, (255, 252, 247)), 540, 1450, 1.0, angle=-2)
    f.alpha_composite(O.DECOR)
    im = f.convert("RGB"); im.save(path_png); im.save(path_png.replace(".png", ".jpg"), quality=92)
    return path_png

if __name__ == "__main__":
    v = make()
    if len(sys.argv) > 1 and sys.argv[1] == "prev":
        ts = [(v.starts[i] + v.ends[i]) / 2 + 0.4 for i in range(len(v.scenes))]
        v.preview(ts, "lutein_prev.jpg"); print([round(x, 1) for x in v.starts], round(v.dur, 1))
    else:
        v.render()
        mus = v.out.replace(".mp4", "_music.mp4"); O.add_music(v, v.out, mus)
        png = cover(OUT + "olga_lutein_cover.png")
        O.with_cover(mus, png, OUT + "olga_lutein_final.mp4")

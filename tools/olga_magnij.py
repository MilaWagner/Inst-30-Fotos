"""Ольга (FitLine), ролик без лица «Магний и судороги» в стиле «видеослайд».
Голос: офлайн-синтез Piper (ru_RU-irina-medium). Запуск: python3 -I olga_magnij.py [prev]"""
import os, sys, subprocess
sys.path.insert(0, "/home/user/Inst-30-Fotos/tools")
from PIL import Image, ImageDraw, ImageFont
import slide_engine as E

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

def _mono():
    o = Image.new("RGBA", (96, 96), (0, 0, 0, 0)); d = ImageDraw.Draw(o)
    d.ellipse((0, 0, 95, 95), fill=(246, 240, 230, 255)); d.ellipse((4, 4, 91, 91), fill=E.CARD_DARK + (255,))
    d.text((48, 50), "О", font=E.HI(56), fill=(214, 180, 150), anchor="mm")
    return o
E.avatar = _mono
def _no_whisper(*a, **k): raise FileNotFoundError
E.whisper_align = _no_whisper

TEXT = ("Вечер. Ты наконец села отдохнуть, и снова сводит ногу. Знакомо? "
        "Причин может быть несколько: мало воды, мало движения, нехватка минералов. "
        "Один из таких минералов — магний. "
        "Магний способствует нормальной работе мышц. И способствует уменьшению усталости. "
        "Я слежу за магнием каждый день. "
        "Если судороги частые, обязательно покажись врачу. "
        "А если хочешь узнать, как это делаю я, напиши мне в личку слово МАГНИЙ.")

def H(*lines): return [list(l) for l in lines]
B, C = "brown", "cream"
SCENES = [
 dict(sents=(0, 3), bg=B, head=H([("Сводит ", 0), ("ноги", 1)], [("по вечерам?", 0)]),
      els=[{"k": "pills", "items": ["вечер", "диван", "и снова судорога"], "x": 540, "y": 860, "step": 200, "size": 64, "at": 0.1, "gap": 0.5}]),
 dict(sents=(3, 4), bg=C, head=H([("Причин ", 0), ("несколько", 1)]),
      els=[{"k": "steps", "items": ["мало воды", "мало движения", "нехватка минералов"], "y": 760, "at": 0.05, "gap": 0.55}]),
 dict(sents=(4, 5), bg=B, head=H([("Один из них — ", 0)], [("магний", 1)]), hsize=110,
      els=[{"k": "cards2", "a": ("Mg", "магний"), "b": ("мышцы", "и энергия"), "y": 860, "at": 0.1}]),
 dict(sents=(5, 7), bg=C, head=H([("Что делает ", 0), ("магний", 1)]),
      els=[{"k": "pills", "items": ["нормальная работа мышц", "меньше усталости"], "x": 540, "y": 860, "step": 210, "size": 58, "at": 0.1, "gap": 0.9}]),
 dict(sents=(7, 8), bg=B, head=H([("Я слежу ", 0)], [("каждый день", 1)]),
      els=[{"k": "steps", "items": ["утро", "мой ритуал", "каждый день"], "y": 760, "at": 0.05, "gap": 0.4}]),
 dict(sents=(8, 9), bg=C, head=H([("Часто? ", 0), ("К врачу", 1)]),
      els=[{"k": "cards2", "a": ("часто", "сводит ноги"), "b": ("врач", "обязательно"), "y": 860, "at": 0.1}]),
 dict(sents=(9, 10), bg=B, head=H([("Напиши ", 0), ("МАГНИЙ", 1)]),
      els=[{"k": "msg", "word": "МАГНИЙ", "y": 900, "at": 0.15}]),
]

def voice(path):
    if os.path.exists(path): return
    subprocess.run([sys.executable, "-m", "piper", "-m", VOICE, "-f", path, "--sentence-silence", "0.35", "--length-scale", "1.05"],
                   input=TEXT.encode(), check=True)

def make():
    a = SP + "audio/olga_magnij.wav"; voice(a)
    return E.Video(0, TEXT, a, SCENES, OUT + "olga_magnij.mp4")

if __name__ == "__main__":
    v = make()
    if len(sys.argv) > 1 and sys.argv[1] == "prev":
        ts = [(v.starts[i] + v.ends[i]) / 2 + 0.4 for i in range(len(v.scenes))]
        v.preview(ts, "olga_prev.jpg"); print([round(x, 1) for x in v.starts], round(v.dur, 1))
    else:
        v.render()

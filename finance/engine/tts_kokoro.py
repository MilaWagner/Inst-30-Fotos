"""Бесплатная озвучка (Kokoro, Apache-2.0) по разделам: sections.json -> sNN.wav.
python3 tts_kokoro.py <sections.json> <out_dir> [voice=am_michael] [speed=0.88]
Модель: kokoro-v1.0.onnx + voices-v1.0.bin (github.com/thewh1teagle/kokoro-onnx, releases model-files-v1.0)
в папке $KOKORO_DIR. Между предложениями добавляется пауза 0.25 с — речь спокойнее.
"""
import json, os, re, sys
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

src, out = sys.argv[1], sys.argv[2]
voice = sys.argv[3] if len(sys.argv) > 3 else "am_michael"
speed = float(sys.argv[4]) if len(sys.argv) > 4 else 0.88
md = os.environ["KOKORO_DIR"]
k = Kokoro(os.path.join(md, "kokoro-v1.0.onnx"), os.path.join(md, "voices-v1.0.bin"))
os.makedirs(out, exist_ok=True)
secs = json.load(open(src))
for i, s in enumerate(secs):
    txt = s.get("tts", s["text"])
    parts = [p for p in re.split(r"(?<=[.?!])\s+", txt) if p.strip()]
    chunks, sr = [], 24000
    for p in parts:
        a, sr = k.create(p, voice=voice, speed=speed, lang="en-gb" if voice.startswith("b") else "en-us")
        chunks += [a, np.zeros(int(sr * 0.25), dtype=a.dtype)]
    audio = np.concatenate(chunks)
    sf.write(os.path.join(out, f"s{i:02d}.wav"), audio, sr)
    print(i, round(len(audio) / sr, 1), "s")

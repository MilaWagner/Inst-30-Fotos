"""Добавляет тихую музыку и мягкие звуки к готовым роликам (видео копируется без перекодирования).
Запуск: python3 -I add_audio.py MUSIC.mp3 [N ...]"""
import sys, subprocess, wave
import numpy as np
sys.path.insert(0, "/home/user/Inst-30-Fotos/tools")
from slide_videos import make, OUT
from slide_engine import S

SR = 44100
def env_decay(n, k): return np.exp(-np.arange(n) / (SR * k))

def pop():
    n = int(SR * 0.12); t = np.arange(n) / SR
    f = 520 + 380 * np.minimum(t / 0.05, 1)
    return 0.22 * np.sin(2 * np.pi * np.cumsum(f) / SR) * env_decay(n, 0.03) * np.minimum(np.arange(n) / 80, 1)

def whoosh():
    n = int(SR * 0.45); rng = np.random.default_rng(1)
    x = rng.standard_normal(n); x = np.convolve(x, np.ones(60) / 60, mode="same")
    e = np.sin(np.linspace(0, np.pi, n)) ** 2
    return 0.45 * x * e

def tick():
    n = int(SR * 0.03); rng = np.random.default_rng(2)
    x = rng.standard_normal(n); x = np.diff(np.concatenate([[0], x]))
    return 0.18 * x * env_decay(n, 0.006)

def strike():
    n = int(SR * 0.2); rng = np.random.default_rng(3)
    x = rng.standard_normal(n); x = np.convolve(x, np.ones(18) / 18, mode="same")
    e = np.linspace(0.2, 1, n) * np.exp(-np.linspace(0, 3, n))
    return 0.5 * x * e

def ding():
    n = int(SR * 1.1); t = np.arange(n) / SR
    x = np.sin(2 * np.pi * 1318 * t) + 0.5 * np.sin(2 * np.pi * 1975 * t) + 0.25 * np.sin(2 * np.pi * 2637 * t)
    return 0.14 * x * env_decay(n, 0.3) * np.minimum(np.arange(n) / 100, 1)

SND = {"pop": pop(), "whoosh": whoosh(), "tick": tick(), "strike": strike(), "ding": ding()}

def events(v):
    ev = []
    for si, sc in enumerate(v.scenes):
        a, b = v.starts[si], v.ends[si]; sdur = b - a
        if si > 0: ev.append((a, "whoosh"))
        for el in sc["els"]:
            t0 = a + 0.2 + min(el.get("at", 0.0) * sdur * 0.5, 0.7) + 0.0
            k = el["k"]
            if k in ("pills", "cross"):
                gap = el.get("gap", 0.3 if k == "pills" else 0.45)
                for i in range(len(el["items"])):
                    ev.append((t0 + i * gap, "pop"))
                    if k == "cross": ev.append((t0 + i * gap + 0.5, "strike"))
            elif k == "cards2": ev += [(t0, "pop"), (t0 + 0.5, "pop")]
            elif k == "photo": ev.append((t0, "pop"))
            elif k == "steps":
                gap = el.get("gap", 0.5)
                for i in range(len(el["items"])): ev.append((t0 + i * gap, "pop"))
            elif k == "msg":
                ev.append((t0, "pop"))
                for j in range(len(el["word"])): ev.append((t0 + 0.5 + (j + 1) / len(el["word"]) * 1.0 - 0.15, "tick"))
                ev.append((t0 + 1.7, "ding"))
    return sorted(ev)

def sfx_wav(v, path):
    total = int((v.total + 0.5) * SR); buf = np.zeros(total)
    for t, kind in events(v):
        s = SND[kind]; i = int(t * SR)
        if i < total: buf[i:i + len(s)] += s[: total - i]
    buf = np.clip(buf, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((buf * 32767).astype(np.int16).tobytes())

def main():
    music = sys.argv[1]
    nums = [int(x) for x in sys.argv[2:]] or list(range(1, 8))
    for n in nums:
        v = make(n)
        sf = S + f"work/sfx_{n}.wav"; sfx_wav(v, sf)
        src = OUT + f"oksana_slide_{n}.mp4"; dst = OUT + f"oksana_slide_{n}_music.mp4"
        tot = v.total
        fc = (f"[1:a]aloop=loop=-1:size=2e9,atrim=0:{tot:.2f},volume=0.14,afade=t=in:d=1.5,afade=t=out:st={tot-2.5:.2f}:d=2.5[m0];"
              f"[0:a]asplit=2[vo][sc];[m0][sc]sidechaincompress=threshold=0.03:ratio=6:attack=30:release=500[m];"
              f"[2:a]volume=0.55[fx];[vo][m][fx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.95[a]")
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", music, "-i", sf, "-filter_complex", fc,
               "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", dst]
        subprocess.check_call(cmd); print(dst)

if __name__ == "__main__":
    main()

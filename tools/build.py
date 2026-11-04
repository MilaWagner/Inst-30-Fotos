import os, re, subprocess, textwrap, sys
from PIL import Image

U = "/root/.claude/uploads/8eb0e0d4-3d28-5e23-be55-de9797cd7607/"
S = "/tmp/claude-0/-home-user-Inst-30-Fotos/8eb0e0d4-3d28-5e23-be55-de9797cd7607/scratchpad/"
OUT = "/home/user/Inst-30-Fotos/videos/"
AUD = S + "audio/"
WORK = S + "work/"
os.makedirs(OUT, exist_ok=True); os.makedirs(WORK, exist_ok=True)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# photo id -> (file, crop center x, crop center y) as fractions
P = {
 1: ("b81d2287-image.jpg", .5, .4), 2: ("782aafa9-image.jpg", .5, .4),
 3: ("71ef4252-image.jpg", .5, .4), 4: ("981fd6ff-image.jpg", .62, .5),
 5: ("b022bf0d-image.jpg", .38, .5), 6: ("1af253e2-image.jpg", .45, .45),
 7: ("e7b84ece-image.jpg", .62, .5), 8: ("b5cc2dd1-image.jpg", .62, .6),
 9: ("9dcf2c11-image.jpg", .6, .45),
}
# video number -> photos
PLAN = {1: [3, 7, 8, 9], 2: [4, 2, 1], 3: [1, 5, 6], 4: [8, 7, 6], 5: [2, 1, 9], 6: [1, 4, 3], 7: [8, 3, 5]}

TEXT = {
1: "Представь: утро, кофе, шум моря. А твой офис — это ноутбук, который ты открываешь, где хочешь. Без будильника, без начальника, без «отпроситься». Это не сказка. Сегодня люди зарабатывают онлайн, просто делясь тем, что знают, и показывая свою жизнь. Начать можно с нуля, и свой продукт для этого не нужен. Если хочешь понять, как это работает, напиши мне в личку слово ХОЧУ. Я расскажу подробнее.",
2: "Я мама троих. Раньше мой день был расписан чужими графиками. Клиенты, записи, время, которое нельзя сдвинуть. Потом я начала осваивать онлайн. Это работа, которую можно встроить в жизнь, а не наоборот. Если ты тоже устала подстраиваться, напиши мне в личку слово ХОЧУ. Расскажу, с чего начать.",
3: "Почему женщине важен свой доход? Не ради роскоши. Ради спокойствия. Когда у тебя есть свои деньги, ты не просишь, не объясняешь и не оправдываешься. Ты выбираешь сама. Свой доход — это внутренняя опора. И сегодня его можно выстроить онлайн, спокойно, шаг за шагом. Хочешь узнать как? Напиши мне в личку слово ХОЧУ, и я расскажу.",
4: "Думаешь, чтобы зарабатывать онлайн, нужно придумать свой курс? Нет. Это самый частый миф, который держит женщин на месте годами. Зайти в диджитал можно и без своего продукта. Нужны контент, понятная система и готовность сделать первый шаг. Хочешь разобраться, с чего начать именно тебе? Напиши мне в личку слово ХОЧУ.",
5: "С возрастом всё меньше хочется производить впечатление. И всё больше хочется жить так, как удобно тебе. Без спешки, без гонки, без вечного «надо». Новый этап — не про начать с нуля. Он про то, чтобы наконец сделать свой выбор. И онлайн даёт эту возможность в любом возрасте. Напиши мне в личку слово ХОЧУ, и я расскажу, как это может выглядеть у тебя.",
6: "Я много лет работала визажистом: руками, по записи, по чужому времени. Это красивая профессия, но она привязывает к месту. Теперь я осваиваю онлайн. Он позволяет работать из любой точки и строить своё, а не только обслуживать чужое. Если тебе знакомо это чувство «хочу по-другому», напиши мне в личку слово ХОЧУ. Расскажу подробнее.",
7: "Ты не опоздала. Я хочу, чтобы ты это услышала. Не нужно идеальных условий, особого образования и уверенности на сто процентов. Нужен один первый шаг. Остальное складывается по дороге. Сегодня этот шаг может быть совсем простым: написать мне. Напиши мне в личку слово ХОЧУ, и мы вместе посмотрим, с чего начать.",
}

W, H, FPS = 1080, 1920, 25

def dur(f):
    return float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]).decode())

def make_still(pid, out):
    fn, cx, cy = P[pid]
    im = Image.open(U + fn).convert("RGB")
    w, h = im.size
    target = W / H
    if w / h > target:
        cw, ch = int(h * target), h
    else:
        cw, ch = w, int(w / target)
    x0 = int(min(max(cx * w - cw / 2, 0), w - cw))
    y0 = int(min(max(cy * h - ch / 2, 0), h - ch))
    im = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((W * 2, H * 2), Image.LANCZOS)
    im.save(out, quality=95)

def phrases(text):
    parts = re.split(r'(?<=[.?!])\s+', text.strip())
    out = []
    for p in parts:
        if len(p) > 60:
            sub = re.split(r'(?<=,)\s+|(?<=:)\s+', p)
            cur = ""
            for s in sub:
                if len(cur) + len(s) + 1 <= 55 or not cur:
                    cur = (cur + " " + s).strip()
                else:
                    out.append(cur); cur = s
            if cur: out.append(cur)
        else:
            out.append(p)
    return out

def build(n):
    audio = AUD + f"v{n}.mp3"
    D = dur(audio) + 0.6
    ph = phrases(TEXT[n])
    tot = sum(len(p) for p in ph)
    t = 0.0
    segs = []
    for p in ph:
        d = (dur(audio)) * len(p) / tot
        segs.append((t, t + d, p)); t += d
    photos = PLAN[n]
    k = len(photos)
    per = D / k
    inputs, filt = [], []
    for i, pid in enumerate(photos):
        still = WORK + f"s{pid}.jpg"
        if not os.path.exists(still): make_still(pid, still)
        inputs += ["-i", still]
        frames = int((per + 0.3) * FPS)
        zin = i % 2 == 0
        YEXPR = 'ih-ih/zoom' if pid == 8 else 'ih/2-(ih/zoom/2)'
        z = f"min(zoom+0.0006,1.18)" if zin else f"if(eq(on,1),1.18,max(zoom-0.0006,1.0))"
        filt.append(f"[{i}:v]zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='{YEXPR}':d={frames}:s={W}x{H}:fps={FPS},setsar=1,format=yuv420p,fade=t=in:st=0:d=0.3[v{i}]")
    chain = "".join(f"[v{i}]" for i in range(k)) + f"concat=n={k}:v=1:a=0[bg]"
    filt.append(chain)
    last = "bg"
    for j, (a, b, p) in enumerate(segs):
        mid = (a + b) / 2
        pidx = min(int(mid / per), k - 1)
        ypos = '0.10' if photos[pidx] == 8 else '0.66'
        lines = textwrap.wrap(p, 22)
        tf = WORK + f"t{n}_{j}.txt"
        open(tf, "w", encoding="utf-8").write("\n".join(lines))
        nxt = f"t{j}"
        filt.append(f"[{last}]drawtext=fontfile={FONT}:textfile={tf}:fontsize=68:fontcolor=white:borderw=4:bordercolor=black@0.85:line_spacing=12:x=(w-text_w)/2:y=h*{ypos}:box=0:enable='between(t,{a:.2f},{b:.2f})'[{nxt}]")
        last = nxt
    out = OUT + f"oksana_{n}.mp4"
    cmd = ["ffmpeg","-y","-loglevel","error"] + inputs + ["-i", audio,
           "-filter_complex", ";".join(filt), "-map", f"[{last}]", "-map", f"{k}:a",
           "-t", f"{D:.2f}", "-c:v","libx264","-preset","medium","-crf","21","-pix_fmt","yuv420p",
           "-c:a","aac","-b:a","160k","-movflags","+faststart", out]
    subprocess.check_call(cmd)
    print(out, f"{D:.1f}s", os.path.getsize(out) // 1024, "KB")

if __name__ == "__main__":
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else range(1, 8)):
        build(n)

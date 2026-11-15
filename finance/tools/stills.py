"""stills.py <episode.py> <vdir> t1,t2,... -> кадры и сводные листы vdir/work/sheetN.png (для проверки перед рендером)"""
import sys, glob, os, subprocess
from PIL import Image
ENGINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine", "explainer.py")
ep, vd, ts = sys.argv[1], sys.argv[2], sys.argv[3]
for f in glob.glob(vd + "/work/still_*.png") + glob.glob(vd + "/work/sheet*.png"): os.remove(f)
subprocess.check_call([sys.executable, ENGINE, ep, vd + "/audio", vd + "/out.mp4", ts])
fs = sorted(glob.glob(vd + "/work/still_*.png"))
for k in range(0, len(fs), 4):
    sh = Image.new("RGB", (1920, 1080), "white")
    for i, f in enumerate(fs[k:k + 4]): sh.paste(Image.open(f).resize((960, 540)), ((i % 2) * 960, (i // 2) * 540))
    sh.save(vd + f"/work/sheet{k // 4}.png")
print(len(fs), "stills")

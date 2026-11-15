"""addhook.py <ep_dir> <sname> <theme> <look> <series> <title> <pre> <hook1> <hook2> [<swap_char_look> ...]
Добавляет в начало раздела 0 фразу-крючок (pre), карточки hook/hook/ident, тему и образ персонажа.
Меняет s<sname>.json (text/tts раздела 0) и <ep_dir>/episode.py. Затем нужно ./tts0.sh <sname> <audio>."""
import json, sys
import os
SP = os.environ.get("FIN_WORK", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "work")) + os.sep
ep_dir, sname, theme, look, series, title, pre, h1, h2 = sys.argv[1:10]
pre = pre.strip() + " "
S = json.load(open(SP + f"s{sname}.json"))
orig = S[0]["text"]
if not orig.startswith(pre.strip()):
    S[0]["text"] = pre + orig; S[0]["tts"] = pre + S[0].get("tts", orig)
    json.dump(S, open(SP + f"s{sname}.json", "w"), ensure_ascii=False)
else:
    orig = orig[len(pre):]
ep = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ep_dir, "episode.py")
ns = {}; exec(open(ep).read(), ns); SEC = ns["SECTIONS"]
SEC[0]["text"] = S[0]["text"]
first = " ".join(orig.split()[:3]); second = " ".join(orig.split()[3:6])
promise = "In the next few minutes" if "In the next few minutes" in pre else pre.split(". ")[1][:22]
b = [x for x in SEC[0]["beats"] if x["type"] not in ("hook", "ident")]
if b[0]["at"] == "^": b[0]["at"] = second
SEC[0]["beats"] = [dict(at="^", type="hook", kicker=series, text=h1),
                   dict(at=promise, type="hook", kicker="In this video", text=h2),
                   dict(at=first, type="ident", series=series, title=title)] + b
alt = sys.argv[10:]
k = 0
for sec in SEC[1:]:
    for x in sec["beats"]:
        if x.get("char") and alt and x["type"] == "say":
            ch = x["char"][:3] + [alt[k % len(alt)]]; k += 1
            if k % 3 == 0: x["char"] = ch
for x in SEC[0]["beats"]: assert x["at"] == "^" or x["at"] in SEC[0]["text"], x["at"]
src = json.dumps(SEC, ensure_ascii=False, indent=1).replace("true", "True").replace("false", "False").replace("null", "None")
open(ep, "w").write(f"# {title} (рубрика {series}, тема {theme})\nTHEME = \"{theme}\"\nLOOK = \"{look}\"\nSECTIONS = {src}\n")
print("ok", [(x["at"][:24], x["type"]) for x in SEC[0]["beats"]][:5])

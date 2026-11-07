"""Озвучка через Gemini TTS (Google AI Studio). Ключ — переменная окружения GEMINI_API_KEY.
Пробы голосов: python3 -I gemini_tts.py samples OUT_DIR
Модель можно сменить переменной GEMINI_TTS_MODEL."""
import base64, json, os, subprocess, sys, urllib.request

MODEL = os.environ.get("GEMINI_TTS_MODEL", "gemini-2.5-flash-preview-tts")
STYLE = "Прочитай тепло, спокойно и доверительно, как подруга, с живой интонацией: "
FEMALE = ["Kore", "Aoede", "Leda", "Sulafat"]

def tts(text, path, voice="Kore", style=STYLE):
    """Синтез в WAV 44.1 кГц (Gemini отдаёт PCM s16le 24 кГц моно), с нормализацией громкости."""
    key = os.environ["GEMINI_API_KEY"]
    body = {"contents": [{"parts": [{"text": style + text}]}],
            "generationConfig": {"responseModalities": ["AUDIO"],
                                 "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voice}}}}}
    req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
                                 data=json.dumps(body).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": key})
    data = json.load(urllib.request.urlopen(req, timeout=180))
    pcm = base64.b64decode(data["candidates"][0]["content"]["parts"][0]["inlineData"]["data"])
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000", "-ac", "1", "-i", "-",
                    "-af", "apad=pad_dur=0.4,loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100", path], input=pcm, check=True)
    return path

if __name__ == "__main__" and len(sys.argv) > 2 and sys.argv[1] == "samples":
    hook = "Вечер... Ты наконец села отдохнуть - и снова сводит ногу. Знакомо?"
    for v in FEMALE:
        p = os.path.join(sys.argv[2], f"gemini_{v}.wav"); tts(hook, p, v); print(p)

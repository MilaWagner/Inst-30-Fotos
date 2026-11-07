#!/usr/bin/env bash
# Восстановление ресурсов для роликов Ольги в папку SP (по умолчанию — $OLGA_SP).
# Запуск: OLGA_SP=/путь/к/scratchpad bash tools/olga_setup.sh
# Музыку (music.mp3, «Deep Liquid Bass») скрипт НЕ качает: она на Google Drive
# (fileId 1U4_dku960c2LNQrPhbB4XgFO915cAGIk) — скачать коннектором и положить в $SP/audio/music.mp3.
set -euo pipefail
SP="${OLGA_SP:?укажи OLGA_SP}"
mkdir -p "$SP"/{fonts,stock,audio,models}
G=https://raw.githubusercontent.com/google/fonts/main/ofl
[ -s "$SP/fonts/Manrope%5Bwght%5D.ttf" ] || curl -sSfL -o "$SP/fonts/Manrope%5Bwght%5D.ttf" "$G/manrope/Manrope%5Bwght%5D.ttf"
[ -s "$SP/fonts/PlayfairDisplay-Italic%5Bwght%5D.ttf" ] || curl -sSfL -o "$SP/fonts/PlayfairDisplay-Italic%5Bwght%5D.ttf" "$G/playfairdisplay/PlayfairDisplay-Italic%5Bwght%5D.ttf"
for id in 4548 48618 36710 47955 13198 43270 13810 12873 14727 41180 14710; do
  [ -s "$SP/stock/$id.mp4" ] || curl -sSfL -o "$SP/stock/$id.mp4" "https://assets.mixkit.co/videos/$id/$id-720.mp4" &
done; wait
[ -s "$SP/models/sh.rnnn" ] || curl -sSfL -o "$SP/models/sh.rnnn" https://raw.githubusercontent.com/GregorR/rnnoise-models/master/somnolent-hogwash-2018-09-01/sh.rnnn
if [ ! -d "$SP/models/vosk-model-tts-ru-0.9-multi" ]; then
  curl -sSfL -o "$SP/models/vosk.zip" https://alphacephei.com/vosk/models/vosk-model-tts-ru-0.9-multi.zip
  (cd "$SP/models" && unzip -q vosk.zip && rm vosk.zip)
fi
pip install -q vosk-tts faster-whisper
# фото продуктов (страница рендерится JS -> Playwright, обрезка по альфе без отражения)
node "$(dirname "$0")/olga_products.js" "$SP"
echo "готово: $SP"; [ -s "$SP/audio/music.mp3" ] || echo "НЕТ музыки: $SP/audio/music.mp3 (скачать с Google Drive)"

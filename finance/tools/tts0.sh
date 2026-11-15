#!/bin/bash
# tts0.sh <name> <audiodir>: переозвучить только раздел 0 (крючок) из work/s<name>.json
T="$(cd "$(dirname "$0")" && pwd)"; W="${FIN_WORK:-$T/../work}"
python3 -c "import json;S=json.load(open('$W/s$1.json'));json.dump(S[:1],open('$W/one_$1.json','w'))"
python3 "$T/../engine/tts_kokoro.py" "$W/one_$1.json" "$W/one_$1" am_michael 0.88 >/dev/null 2>&1
cp "$W"/one_$1/s00.* "$2"/ && rm -rf "$W/one_$1" "$W/one_$1.json" && echo "s00 ok $1"

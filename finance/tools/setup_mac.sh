#!/bin/bash
# Установка на macOS (один раз): ffmpeg, Python-библиотеки, модель голоса Kokoro.
set -e
T="$(cd "$(dirname "$0")" && pwd)"
command -v brew >/dev/null || { echo "Сначала установите Homebrew: https://brew.sh"; exit 1; }
brew install python ffmpeg
python3 -m venv "$T/../.venv"
"$T/../.venv/bin/pip" install --upgrade pip
"$T/../.venv/bin/pip" install pillow numpy soundfile kokoro-onnx
M="$HOME/kokoro-models"; mkdir -p "$M"
[ -f "$M/kokoro-v1.0.onnx" ] || curl -L -o "$M/kokoro-v1.0.onnx" https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
[ -f "$M/voices-v1.0.bin" ] || curl -L -o "$M/voices-v1.0.bin" https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
mkdir -p "$T/../work"
grep -q KOKORO_DIR ~/.zshrc 2>/dev/null || echo "export KOKORO_DIR=\"$M\"" >> ~/.zshrc
echo "Готово. Откройте новое окно Терминала и выполните: source $T/../.venv/bin/activate"

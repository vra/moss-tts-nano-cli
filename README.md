# moss-tts-nano-cli

One-command zero-shot voice cloning with the [MOSS-TTS-Nano-100M](https://huggingface.co/mlx-community/MOSS-TTS-Nano-100M) model, powered by [mlx-audio](https://github.com/Blaizzy/mlx-audio).

## Features

- **No manual setup**: `uvx moss-tts-nano-cli` installs the environment automatically.
- **Lazy model download**: the model is fetched from Hugging Face on first use.
- **Voice cloning**: pass a reference WAV and text to synthesize speech in that voice.
- **Apple Silicon optimized**: runs on MLX.

## Requirements

- Python 3.12+
- macOS with Apple Silicon (MLX backend)
- [uv](https://docs.astral.sh/uv/) (recommended)
- FFmpeg (used indirectly by audio tooling)

## Install

```bash
uv tool install moss-tts-nano-cli
```

Or run without installing:

```bash
uvx --from moss-tts-nano-cli moss-tts-nano --help
```

## Usage

### Clone a voice

```bash
moss-tts-nano clone \
  --ref ./my_voice.wav \
  --text "Hello, this is my cloned voice speaking." \
  --out output.wav
```

The first run downloads `mlx-community/MOSS-TTS-Nano-100M` and the audio tokenizer into the Hugging Face cache (`~/.cache/huggingface`).

### Eagerly download the model

```bash
moss-tts-nano download
```

### Show info

```bash
moss-tts-nano info
```

## Development

```bash
git clone https://github.com/vra/moss-tts-nano-cli.git
cd moss-tts-nano-cli
uv sync --extra dev
uv run pytest
```

## License

MIT

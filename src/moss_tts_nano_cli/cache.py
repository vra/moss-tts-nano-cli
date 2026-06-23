"""Cache and path helpers for the MOSS-TTS-Nano CLI."""

from pathlib import Path

DEFAULT_MODEL_ID = "mlx-community/MOSS-TTS-Nano-100M"


def default_cache_dir() -> Path:
    """Return the default Hugging Face cache directory used by mlx-audio."""
    return Path.home() / ".cache" / "huggingface"

"""Text-to-speech inference helpers for MOSS-TTS-Nano."""

from pathlib import Path

import numpy as np
import soundfile as sf
from mlx_audio.tts.utils import load_model

from moss_tts_nano_cli.cache import DEFAULT_MODEL_ID


def load_reference_audio(path: Path) -> tuple[np.ndarray, int]:
    """Load a reference WAV file and return mono audio + sample rate."""
    audio, sample_rate = sf.read(str(path))
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    return audio.astype(np.float32), int(sample_rate)


def clone_voice(
    text: str,
    ref_audio_path: Path,
    model_id: str = DEFAULT_MODEL_ID,
    verbose: bool = True,
):
    """Generate speech cloned from *ref_audio_path* speaking *text*.

    Returns the generated waveform as a NumPy array and the model sample rate.
    """
    ref_audio, ref_sr = load_reference_audio(ref_audio_path)
    if verbose:
        print(f"Loaded reference audio: {ref_audio.shape[0]} samples @ {ref_sr} Hz")

    if verbose:
        print(f"Loading model {model_id!r}... (first run will download files)")
    model = load_model(model_id)
    if verbose:
        print(f"Model loaded; sample rate = {model.sample_rate} Hz")

    if verbose:
        print(f"Generating speech for: {text!r}")
    results = list(
        model.generate(
            text=text,
            ref_audio=ref_audio,
            ref_audio_sample_rate=ref_sr,
        )
    )
    result = results[0]
    audio = np.array(result.audio)
    if verbose:
        print(
            f"Generated {audio.shape[0]} samples "
            f"({result.audio_duration}) @ {result.sample_rate} Hz "
            f"RTF={result.real_time_factor:.3f}"
        )
    return audio, int(result.sample_rate)


def save_audio(path: Path, audio: np.ndarray, sample_rate: int) -> None:
    """Save a waveform to a WAV file."""
    sf.write(str(path), audio, sample_rate)

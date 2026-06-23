"""Command-line interface for MOSS-TTS-Nano."""

from importlib.metadata import version
from pathlib import Path

import click

from moss_tts_nano_cli.cache import DEFAULT_MODEL_ID, default_cache_dir
from moss_tts_nano_cli.tts import clone_voice, save_audio


@click.group()
@click.version_option(version=version("moss-tts-nano-cli"), prog_name="moss-tts-nano")
def cli():
    """MOSS-TTS-Nano CLI: zero-shot multilingual voice cloning."""


@cli.command()
@click.option(
    "--ref",
    "ref_path",
    required=True,
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    help="Path to the reference WAV audio file for voice cloning.",
)
@click.option(
    "--text",
    required=True,
    help="Text to synthesize in the cloned voice.",
)
@click.option(
    "--out",
    "out_path",
    default="output.wav",
    show_default=True,
    type=click.Path(path_type=Path),
    help="Output WAV file path.",
)
@click.option(
    "--model",
    "model_id",
    default=DEFAULT_MODEL_ID,
    show_default=True,
    help="Hugging Face model id for MOSS-TTS-Nano.",
)
@click.option(
    "--quiet",
    is_flag=True,
    help="Suppress progress messages.",
)
def clone(ref_path: Path, text: str, out_path: Path, model_id: str, quiet: bool) -> None:
    """Clone a voice from REF audio and speak TEXT."""
    audio, sample_rate = clone_voice(
        text=text,
        ref_audio_path=ref_path,
        model_id=model_id,
        verbose=not quiet,
    )
    save_audio(out_path, audio, sample_rate)
    click.echo(f"Saved output to {out_path}")


@cli.command()
@click.option(
    "--model",
    "model_id",
    default=DEFAULT_MODEL_ID,
    show_default=True,
    help="Hugging Face model id for MOSS-TTS-Nano.",
)
def download(model_id: str) -> None:
    """Eagerly download the model and audio tokenizer."""
    click.echo(f"Downloading model {model_id!r}...")
    from mlx_audio.tts.utils import load_model

    load_model(model_id)
    click.echo("Model download complete.")


@cli.command()
def info() -> None:
    """Show cache location, default model, and package metadata."""
    click.echo(f"Default model: {DEFAULT_MODEL_ID}")
    click.echo(f"Cache directory: {default_cache_dir()}")
    click.echo("Commands: clone, download, info")


def main() -> None:
    cli()

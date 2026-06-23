"""Smoke tests for the CLI entry points."""

from click.testing import CliRunner

from moss_tts_nano_cli.cli import cli


def test_info_command():
    runner = CliRunner()
    result = runner.invoke(cli, ["info"])
    assert result.exit_code == 0
    assert "Default model" in result.output


def test_clone_requires_ref_and_text():
    runner = CliRunner()
    result = runner.invoke(cli, ["clone"])
    assert result.exit_code != 0
    assert "Missing option" in result.output

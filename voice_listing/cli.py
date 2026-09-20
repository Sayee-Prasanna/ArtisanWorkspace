"""
Voice & Listing Generation CLI
===============================
CLI entry point for Workstream 3.

Commands
--------
  transcribe   Transcribe audio to text (Bhashini ASR)
  translate    Translate text between languages (Bhashini NMT)
  tts          Generate speech from text (Bhashini TTS)
  listing      Full pipeline: audio → transcript → translate → listing

Usage
-----
  python cli.py transcribe audio.wav --lang hi
  python cli.py translate "नमस्ते" --from hi --to en
  python cli.py tts "Hello world" --lang en --output hello.wav
  python cli.py listing audio.wav --lang hi --tags '{"craft_type":"Pottery","material":"Terracotta","category":"Home Decor"}'
  python cli.py listing --mock   # run with mock data (no API keys needed)
"""

import os
import sys

# Fix Windows console encoding for Unicode/emoji output
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


import json
import click
from pathlib import Path


@click.group()
@click.version_option(version="0.1.0", prog_name="voice-listing")
def cli():
    """🎤 Voice & Listing Generation CLI — Workstream 3"""
    pass


# ── transcribe ───────────────────────────────────────────────────────
@cli.command()
@click.argument("audio_file", type=click.Path(exists=True))
@click.option(
    "--lang", "-l", default="hi", help="Source language code (e.g. hi, ta, te)"
)
@click.option("--mock", is_flag=True, help="Use mock data instead of live API")
def transcribe(audio_file, lang, mock):
    """Transcribe an audio file to text using Bhashini ASR."""
    if mock:
        from mock_data import mock_transcribe

        result = mock_transcribe(lang)
        click.echo(json.dumps(result, ensure_ascii=False, indent=2))
        return

    from bhashini_client import BhashiniClient

    client = BhashiniClient()
    transcript = client.speech_to_text(audio_file, source_lang=lang)
    result = {"transcript": transcript, "source_lang": lang}
    click.echo(json.dumps(result, ensure_ascii=False, indent=2))


# ── translate ────────────────────────────────────────────────────────
@cli.command()
@click.argument("text")
@click.option("--from", "from_lang", default="hi", help="Source language code")
@click.option("--to", "to_lang", default="en", help="Target language code")
@click.option("--mock", is_flag=True, help="Use mock data instead of live API")
def translate(text, from_lang, to_lang, mock):
    """Translate text between languages using Bhashini NMT."""
    if mock:
        from mock_data import mock_translate

        result = mock_translate(text, from_lang, to_lang)
        click.echo(json.dumps(result, ensure_ascii=False, indent=2))
        return

    from bhashini_client import BhashiniClient

    client = BhashiniClient()
    translated = client.translate(text, source_lang=from_lang, target_lang=to_lang)
    result = {
        "source_text": text,
        "translated_text": translated,
        "source_lang": from_lang,
        "target_lang": to_lang,
    }
    click.echo(json.dumps(result, ensure_ascii=False, indent=2))


# ── tts ──────────────────────────────────────────────────────────────
@cli.command()
@click.argument("text")
@click.option("--lang", "-l", default="hi", help="Language code for speech")
@click.option(
    "--output", "-o", default="output.wav", help="Output audio file path"
)
@click.option("--mock", is_flag=True, help="Use mock data instead of live API")
def tts(text, lang, output, mock):
    """Generate speech from text using Bhashini TTS."""
    if mock:
        from mock_data import mock_tts

        result = mock_tts(text, lang)
        click.echo(json.dumps(result, ensure_ascii=False, indent=2))
        return

    from bhashini_client import BhashiniClient

    client = BhashiniClient()
    saved_path = client.text_to_speech(text, lang=lang, output_path=output)
    result = {"text": text, "lang": lang, "audio_file": saved_path}
    click.echo(json.dumps(result, ensure_ascii=False, indent=2))
    click.echo(f"\n✅ Audio saved to: {saved_path}", err=True)


# ── listing (full pipeline) ─────────────────────────────────────────
@cli.command()
@click.argument("audio_file", required=False, type=click.Path(exists=True))
@click.option(
    "--lang", "-l", default="hi", help="Source language of the audio"
)
@click.option(
    "--tags",
    "-t",
    default=None,
    help='Image tags as JSON string, e.g. \'{"craft_type":"Pottery","material":"Terracotta","category":"Home Decor"}\'',
)
@click.option(
    "--speak", is_flag=True, help="Read the generated listing aloud via TTS"
)
@click.option("--mock", is_flag=True, help="Run entire pipeline with mock data")
@click.option(
    "--output-tts",
    default="listing_readout.wav",
    help="Output path for TTS audio (used with --speak)",
)
def listing(audio_file, lang, tags, speak, mock, output_tts):
    """Full pipeline: audio → transcribe → translate → generate listing.

    \b
    Examples:
      python cli.py listing audio.wav --lang hi --tags '{"craft_type":"Pottery"}'
      python cli.py listing --mock
    """
    if mock:
        from mock_data import mock_listing

        result = mock_listing()
        click.echo(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if not audio_file:
        click.echo(
            "Error: AUDIO_FILE is required when not using --mock.", err=True
        )
        sys.exit(1)

    # Parse image tags
    if tags:
        try:
            image_tags = json.loads(tags)
        except json.JSONDecodeError:
            click.echo("Error: --tags must be valid JSON.", err=True)
            sys.exit(1)
    else:
        image_tags = {
            "craft_type": "Handicraft",
            "material": "Mixed",
            "category": "Home Decor",
        }

    from bhashini_client import BhashiniClient
    from listing_generator import generate_listing

    client = BhashiniClient()

    # Step 1 + 2: Transcribe and translate
    click.echo("🎤 Transcribing and translating audio...", err=True)
    stt_result = client.speech_to_text_and_translate(
        audio_file, source_lang=lang, target_lang="en"
    )
    transcript = stt_result["transcript"]
    translated = stt_result["translated_text"]
    click.echo(f"📝 Transcript: {transcript}", err=True)
    click.echo(f"🌐 Translation: {translated}", err=True)

    # Step 3: Generate listing
    click.echo("📄 Generating listing...", err=True)
    listing_data = generate_listing(translated, image_tags)

    # Build the full response (matching API contract)
    result = {
        "transcript": transcript,
        "translated_text": translated,
        "listing": listing_data,
        "audio_alert_url": None,
    }

    # Step 4 (optional): TTS readout
    if speak:
        click.echo("🔊 Generating TTS readout...", err=True)
        tts_text = f"{listing_data.get('title', '')}. {listing_data.get('description', '')}"
        saved = client.text_to_speech(tts_text, lang="en", output_path=output_tts)
        result["audio_alert_url"] = saved
        click.echo(f"✅ TTS audio saved to: {saved}", err=True)

    # Output the final JSON
    click.echo(json.dumps(result, ensure_ascii=False, indent=2))


# ── entry point ──────────────────────────────────────────────────────
if __name__ == "__main__":
    cli()

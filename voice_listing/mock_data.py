"""
Mock Data Layer
===============
Hardcoded mock responses matching the API contracts from COLLABORATION_PLAN.md.
Other workstreams can import these to test their integrations without needing
live Bhashini or Gemini credentials.
"""


def mock_transcribe(source_lang: str = "hi") -> dict:
    """Return a mock ASR (speech-to-text) response."""
    transcripts = {
        "hi": "यह एक सुंदर मिट्टी का बर्तन है जो मैंने अपने हाथों से बनाया है। "
              "इसमें पारंपरिक राजस्थानी डिज़ाइन है और इसे प्राकृतिक रंगों से सजाया गया है।",
        "ta": "இது ஒரு அழகான மண் பானை, நான் என் கைகளால் செய்தேன்.",
        "te": "ఇది ఒక అందమైన మట్టి కుండ, నేను నా చేతులతో తయారు చేసాను.",
    }
    return {
        "transcript": transcripts.get(source_lang, transcripts["hi"]),
        "source_lang": source_lang,
    }


def mock_translate(
    text: str = None, source_lang: str = "hi", target_lang: str = "en"
) -> dict:
    """Return a mock NMT (translation) response."""
    return {
        "source_text": text or mock_transcribe(source_lang)["transcript"],
        "translated_text": (
            "This is a beautiful clay pot that I made with my own hands. "
            "It has a traditional Rajasthani design and is decorated with natural colours."
        ),
        "source_lang": source_lang,
        "target_lang": target_lang,
    }


def mock_tts(text: str = None, lang: str = "hi") -> dict:
    """Return a mock TTS response (no real audio)."""
    return {
        "text": text or "यह एक सुंदर मिट्टी का बर्तन है।",
        "lang": lang,
        "audio_url": "mock://tts-output.wav",
        "message": "Mock TTS — no audio generated. Use live Bhashini for real audio.",
    }


def mock_listing() -> dict:
    """
    Return a mock listing that matches the API contract
    defined in COLLABORATION_PLAN.md section B.
    """
    return {
        "transcript": "यह एक सुंदर मिट्टी का बर्तन है जो मैंने अपने हाथों से बनाया है।",
        "translated_text": (
            "This is a beautiful clay pot that I made with my own hands. "
            "It has a traditional Rajasthani design and is decorated with natural colours."
        ),
        "listing": {
            "title": "Handcrafted Terracotta Clay Pot — Rajasthani Design",
            "description": (
                "This exquisite terracotta clay pot is handcrafted by skilled "
                "Rajasthani artisans using centuries-old pottery techniques. "
                "Decorated with traditional motifs and natural earth-toned colours, "
                "each piece is a unique work of art. Perfect for home decor, "
                "indoor plants, or as a statement piece that celebrates India's "
                "rich craft heritage."
            ),
            "seo_tags": [
                "terracotta",
                "pottery",
                "handmade",
                "rajasthani",
                "clay pot",
                "home decor",
                "artisan",
                "traditional craft",
                "indian handicraft",
                "natural colours",
            ],
        },
        "audio_alert_url": "mock://tts-listing-readout.mp3",
    }


def mock_image_tags() -> dict:
    """Return mock image tags (from Workstream 2: Vision API)."""
    return {
        "craft_type": "Pottery",
        "material": "Terracotta",
        "category": "Home Decor",
    }

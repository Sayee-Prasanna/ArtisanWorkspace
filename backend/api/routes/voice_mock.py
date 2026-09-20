from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VoiceListingRequest(BaseModel):
    audio_url: str
    image_tags: dict
    language: str

@router.post("/listing")
def voice_listing(req: VoiceListingRequest):
    return {
        "transcript": "यह एक सुंदर मिट्टी का बर्तन है...",
        "translated_text": "This is a beautiful clay pot...",
        "listing": {
            "title": "Handcrafted Terracotta Clay Pot",
            "description": "Authentic handcrafted terracotta pot perfect for home decor.",
            "seo_tags": ["terracotta", "pottery", "handmade", "decor"]
        },
        "audio_alert_url": "https://storage.../tts-alert.mp3"
    }

from fastapi import APIRouter

router = APIRouter()

@router.get("/match")
def match_schemes(artisan_id: str):
    return {
        "eligible_schemes": [
            {
                "scheme_id": "sch_01",
                "name": "PM Vishwakarma Yojana",
                "benefit": "Subsidized loan up to ₹1 Lakh",
                "audio_summary_url": "https://storage.../scheme-audio.mp3"
            }
        ]
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from api.routes import auth, khata, schemes, passport, vision_mock, voice_mock, pricing_mock
from core.config import settings
import os

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(khata.router, prefix="/api/khata", tags=["Digital Khata"])
app.include_router(schemes.router, prefix="/api/schemes", tags=["Schemes"])
app.include_router(passport.router, prefix="/api/passport", tags=["Craft Passport"])
app.include_router(vision_mock.router, prefix="/api/vision", tags=["Vision Studio (Mock)"])
app.include_router(voice_mock.router, prefix="/api/voice", tags=["Voice & Listing (Mock)"])
app.include_router(pricing_mock.router, prefix="/api/pricing", tags=["Pricing & Market (Mock)"])

@app.get("/")
def root():
    return {"message": "Welcome to Artisan Workspace API. Go to /docs for Swagger UI."}

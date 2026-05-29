from fastapi import APIRouter

from backend.api.v1.audio import router as audio_router

router = APIRouter(prefix="/v1")

router.include_router(audio_router, prefix="/audio", tags=["audio"])

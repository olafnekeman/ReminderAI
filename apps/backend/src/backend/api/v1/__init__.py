from fastapi import APIRouter

from backend.api.v1 import audio, messages

router = APIRouter(prefix="/v1")

router.include_router(audio.router, prefix="/audio", tags=["audio"])
router.include_router(messages.router, prefix="/messages", tags=["messages"])

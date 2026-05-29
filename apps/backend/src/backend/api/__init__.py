from fastapi import APIRouter

from backend.api import docs, v1

router = APIRouter()

router.include_router(docs.router, prefix="/docs", tags=["docs"])
router.include_router(v1.router, prefix="/v1", tags=["v1"])

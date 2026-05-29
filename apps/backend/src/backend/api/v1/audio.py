from fastapi import APIRouter

router = APIRouter()


@router.get(path="")
def get_audio():
    return {"message": "Hello, World!"}


@router.post(path="")
def post_audio():
    return {"message": "Hello, World!"}

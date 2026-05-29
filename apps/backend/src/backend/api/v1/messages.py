from fastapi import APIRouter

router = APIRouter()


@router.post(path="")
def create_message():
    return {"message": "Hello, World!"}

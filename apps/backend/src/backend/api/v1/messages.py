from fastapi import APIRouter
from pydantic import BaseModel
from backend.schemas import Message
import uuid
import datetime as dt

router = APIRouter()


# ---------------------------------------------------------------------------
# POST /messages
# ---------------------------------------------------------------------------


class CreateMessage(BaseModel):
    content: str


@router.post(path="")
def create_message(message: CreateMessage) -> Message:
    return Message(
        id=uuid.uuid4(),
        created_at=dt.datetime.now(dt.UTC),
        role="user",
        content=message.content,
    )

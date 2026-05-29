from pydantic import BaseModel
import datetime as dt
import uuid


class Message(BaseModel):
    id: uuid.UUID
    created_at: dt.datetime
    role: str
    content: str

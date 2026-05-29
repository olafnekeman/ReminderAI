from backend.api.v1.messages import CreateMessage, Message
import httpx


client = httpx.Client(
    base_url="http://localhost:8000",
)


def create_message(content: str) -> Message:
    data = CreateMessage(content=content)

    response = client.post(
        "http://localhost:8000/v1/messages",
        json=data.model_dump(mode="json"),
    )
    response.raise_for_status()
    data = response.json()
    return Message.model_validate(data)

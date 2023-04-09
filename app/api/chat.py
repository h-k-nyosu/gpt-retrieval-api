from fastapi import APIRouter, HTTPException
from app.services.chat_service import ChatService

router = APIRouter()


@router.get("/chat")
async def chat(message: str) -> dict:
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    service = ChatService()
    return {"response": service.chat(message)}

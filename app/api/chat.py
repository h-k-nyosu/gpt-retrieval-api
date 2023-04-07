from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/chat")
async def chat(message: str) -> dict:
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    response = f"You sent: {message}"
    return {"response": response}
from typing import List
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

@router.post("/index")
async def chat(urls: List[str] = Query(default=None)) -> dict:
    if not urls:
        raise HTTPException(status_code=400, detail="Urls cannot be empty")

    response = f"You sent: {urls}"
    return {"response": response}
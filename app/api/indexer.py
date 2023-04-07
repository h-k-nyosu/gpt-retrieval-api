from typing import List
from fastapi import APIRouter, HTTPException, Query
from app.services.indexer_service import index

router = APIRouter()

@router.post("/index")
async def chat(urls: List[str] = Query(default=None)) -> dict:
    if not urls:
        raise HTTPException(status_code=400, detail="Urls cannot be empty")
    
    status, message = index(urls)
    return {"status": status, "message": message}
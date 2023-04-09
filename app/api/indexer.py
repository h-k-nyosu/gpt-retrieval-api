from typing import List
from fastapi import APIRouter, HTTPException, Query
from app.services.indexer_service import index
from pydantic import BaseModel

router = APIRouter()


class Urls(BaseModel):
    urls: List[str]


@router.post("/index")
async def chat(url_data: Urls) -> dict:
    urls = url_data.urls
    if not urls:
        raise HTTPException(status_code=400, detail="Urls cannot be empty")

    status, message = index(urls)
    return {"status": status, "message": message}

import os
from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.chat import router as chat_router
from app.api.indexer import router as indexer_router


load_dotenv()

# 環境変数を読み取る例
api_key = os.environ["OPENAI_API_KEY"]

app = FastAPI()

app.include_router(chat_router, prefix="/api")
app.include_router(indexer_router, prefix="/api")
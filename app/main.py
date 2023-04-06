import os
from fastapi import FastAPI
from dotenv import load_dotenv

from app.api import router as api_router


load_dotenv()

# 環境変数を読み取る例
api_key = os.environ["OPENAI_API_KEY"]

app = FastAPI()

app.include_router(api_router, prefix="/api")
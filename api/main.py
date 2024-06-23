from fastapi import FastAPI
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)

@app.get("/")
async def root():
    return {
        "message": str(datetime.now()),
        "status": 200,
    }
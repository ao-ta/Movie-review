from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)

app.message = ""
a = 0


@app.get("/message/len")
async def get_message():
    a = len(app.message)
    return {
        "message": a,
        "status": 200,
    }


@app.post("/message/len")
async def post_message(message):
    app.message = message
    return {
        "message": app.message,
        "status": 200,
    }
    


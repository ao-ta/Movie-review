from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)

app.message1 = ""
app.message2 = ""


@app.get("/message")
async def get_message():

    return {
        "message": app.message2,
        "status": 200,
    }


@app.post("/message")
async def post_message(message):
    if 'clear' in message:
        app.message1 = message
        app.message2 = ""
    else:
        app.message1 = message
        app.message2 += message
    return {
        "message": app.message1,
        "status": 200,
    }
    


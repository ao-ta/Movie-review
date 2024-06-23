from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

import api.schemas.message as message_schema
from datetime import datetime

from pydantic import ValidationError

from api.misc.lock import lock, unlock


app = FastAPI()
app.message = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)


@app.get("/", response_class=HTMLResponse)
async def get_client():
    data = ''
    with open('client.html', 'rt', encoding='utf-8') as f:
        data = f.read()
    return data


def load():
    try:
        lock()
        with open('data.json', 'rt', encoding='utf-8') as f:
            app.message = message_schema.Message.parse_raw(f.read())
    except (FileNotFoundError, ValidationError):
        # ファイルが存在しない or ファイルがうまく読めない
        # →Default の Message を作成する
        app.message = message_schema.Message()
    finally:
        unlock()


async def save():
    try:
        lock()
        with open('data.json', 'wt', encoding='utf-8') as f:
            f.write(app.message.model_dump_json(indent=4))
    finally:
        unlock()


@app.get("/message", response_model=message_schema.Message)
async def get_message():
    return app.message


@app.post("/message", response_model=message_schema.Message)
async def post_message(message: message_schema.MessageBase):
    m = message_schema.Message(time=datetime.now(),
                               **message.dict())
    app.message = m
    await save()
    return m


load()
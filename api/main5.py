from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api.schemas.message as message_schema
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['null'],
    allow_methods=['*'],
)

app.message = message_schema.Message()


@app.get("/message", response_model=message_schema.Message)
def get_message():
    return app.message


@app.post("/message", response_model=message_schema.Message)
def post_message(message: message_schema.MessageBase):
    app.message = message_schema.Message(time=datetime.now(),
                                         **message.dict())
    return app.message
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from predict import predict

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/text/{text}")
def read_item(text: str):
    return {"text": text, "embedding": predict(text)}

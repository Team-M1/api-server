from fastapi import FastAPI
from pydantic import BaseModel

from model.predict import predict


app = FastAPI()


class Text(BaseModel):
    text: str


@app.get("/")
async def root():
    message = """악플탐지 API의 메인 페이지입니다.
예측을 하려면 /predict/{문장}으로 GET 요청을 보내거나,
/predict에 {'text': 문장}으로 POST 요청을 보내길 바랍니다."""
    return message.replace("\n", " ")


@app.get("/predict/{text}")
async def inference_get(text: str):
    """'/predict/{text}'에 대한 GET 요청에 대응하는 함수"""
    d = {"text": text}
    pred = await predict(text)
    d.update(pred)
    return d


@app.post("/predict")
async def inference_post(text: Text):
    """'/predict'에 대한 POST 요청에 대응하는 함수"""
    d = {"text": text.text}
    pred = await predict(text.text)
    d.update(pred)
    return d

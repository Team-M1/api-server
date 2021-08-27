from fastapi import FastAPI

from predict import predict


app = FastAPI()


@app.get("/")
async def root():
    return "악플탐지 API의 메인 페이지입니다. 예측을 하려는 경우 /text/{문장}으로 요청을 보내시길 바랍니다."


@app.get("/text/{text}")
async def read_item(text: str):
    return {"text": text, "embedding": predict(text)}

from fastapi import FastAPI

from model.predict import predict


app = FastAPI()


@app.get("/")
async def root():
    return "악플탐지 API의 메인 페이지입니다. 예측을 하려는 경우 /predict/{문장}으로 요청을 보내시길 바랍니다."


@app.get("/predict/{text}")
async def inference(text: str):
    d = {"text": text}
    pred = await predict(text)
    d.update(pred)
    return d

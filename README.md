# korean-malicious-comments-api (kmca)

FastAPI 기반 한국어 악플 탐지기 서버



## 사용방법

#### 1. 도커

```sh
docker run -d -p 80:80 ks2515/kmca
```

도커를 통해 간편하게 서버를 시작할 수 있습니다.

[tiangolo/uvicorn-gunicorn](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn) 이미지를 베이스로 하므로 해당 이미지에서 사용가능한 환경변수를 모두 사용할 수 있습니다. 예) `HOST`, `PORT`, `MAX_WORKERS` 등

자세한 내용은 해당 문서를 참고하시길 바랍니다.



#### 2. heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

위의 버튼을 누르는 것으로 heroku를 통해서 실행할 수 있습니다.



#### 3. 로컬

```sh
uvicorn main:app
```

터미널에서 위 명령어를 사용하여 uvicorn을 사용하여 로컬에서 서버를 실행할 수 있습니다.

자세한 사항은 [FastAPI 공식문서](https://fastapi.tiangolo.com/deployment/manually/)의 해당 내용과 [uvicorn 공식문서](https://www.uvicorn.org/)를 참고하시길 바랍니다.

## API

[Wiki](https://github.com/Team-M1/korean-malicious-comments-api/wiki/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%83%81%EC%84%B8-%EC%84%A4%EB%AA%85#api)를 참고하시기 바랍니다.

## 사용 모델 

[monologg/KoCharELECTRA](https://github.com/monologg/KoCharELECTRA)를 사용하여 전이학습한 모델을 사용합니다.

모델 훈련 과정은 [Team-M1/badwords-classifier-train](https://github.com/Team-M1/badwords-classifier-train) 이 저장소에서,

사용한 데이터는 [Team-M1/community-comments-csv-data](https://github.com/Team-M1/community-comments-csv-data) 여기서 확인하실 수 있습니다.

## Reference

<https://fastapi.tiangolo.com/>

<https://github.com/tiangolo/uvicorn-gunicorn-docker>
# korean-malicious-comments-api

fastAPI 기반 한국어 악플 탐지기 서버

## Getting started

CLI에서 `uvicorn main:app` 명령어를 사용하여 localhost 에서 서버를 실행할 수 있습니다. 만약 개발 목적 등으로 핫리로드를 사용하고 싶다면 `uvicorn main:app --reload` 명령어를 사용하시기 바랍니다.

## API

[Wiki](https://github.com/Team-M1/korean-malicious-comments-api/wiki/1%EC%A3%BC%EC%B0%A8-%EB%AF%B8%EC%85%98)를 참고하시기 바랍니다.

## heroku

엔드포인트: <https://kmca.herokuapp.com/>

위 엔드포인트는 개발용이며 최종 배포용이 나올 때까지는 필요할때마다 열어서 사용할 예정입니다.

heroku 로 배포하기 위해서는 다음 명령어를 수행하시기 바랍니다. 단, 반드시 `master` 브랜치로 배포되어야 하므로 현재 작업중인 브랜치에서 `master` 브랜치를 새로 checkout 한 후 다음 명령어를 수행하면 됩니다.

```s
heroku git:remote kmca
heroku stack:set container
git push heroku master
```

현재 heroku worker 에서 메모리가 부족한 R14 이슈가 존재하므로 worker 의 수를 1로 제한했습니다.

```s
heroku config:set WEB_CONCURRENCY=1
```

## Reference

<https://github.com/askblaker/fastapi-docker-heroku>

<https://devcenter.heroku.com/>

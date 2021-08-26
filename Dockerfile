FROM tiangolo/uvicorn-gunicorn:python3.8

RUN pip install --no-cache-dir fastapi
RUN pip install --no-cache-dir torch
RUN pip install --no-cache-dir transformers

COPY . /app
WORKDIR /app

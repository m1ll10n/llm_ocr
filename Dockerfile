FROM python:3.12-slim

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
  && pip install torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cpu \
  && pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

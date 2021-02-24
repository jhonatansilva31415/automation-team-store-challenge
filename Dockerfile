FROM python:3.9.0-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

COPY . .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh
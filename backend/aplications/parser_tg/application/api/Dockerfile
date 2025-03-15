FROM python:3.11-slim-buster as backend

RUN apt-get update
RUN pip install --upgrade pip

COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r /backend/requirements.txt

COPY backend/aplications/parser_tg/ /backend/aplications/parser_tg


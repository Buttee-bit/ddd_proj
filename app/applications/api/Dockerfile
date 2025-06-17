FROM python:3.11-slim-buster AS api

RUN apt-get update
RUN pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY app/ /app/


COPY MyAppNewsNow.session ./MyAppNewsNow.session
COPY MyAppNewsNow.session-journal ./MyAppNewsNow.session-journal
COPY ./.env /app/.env
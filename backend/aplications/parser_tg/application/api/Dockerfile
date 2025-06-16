FROM python:3.11-slim-buster AS backend

RUN apt-get update
RUN pip install --upgrade pip

COPY ./requirements.txt /backend/requirements.txt

RUN pip install -r /backend/requirements.txt

COPY backend/aplications/parser_tg/ /backend/aplications/parser_tg
COPY backend/pullenti/ /backend/pullenti

COPY MyAppNewsNow.session ./MyAppNewsNow.session
COPY MyAppNewsNow.session-journal ./MyAppNewsNow.session-journal
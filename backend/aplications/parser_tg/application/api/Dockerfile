FROM python:3.11-slim-buster as backend

RUN apt-get update


COPY ./requirements.txt /backend/requirements.txt
COPY backend/aplications/parser_tg/ /backend/aplications/parser_tg

RUN pip install --upgrade pip
RUN pip install -r /backend/requirements.txt


# COPY ../api /app/api
# COPY ../shared /app/shared
# RUN pip install -r /shared/requirements.txt


# ENV PYTHONPATH "${PYTHONPATH}:/backend"
# WORKDIR /backend
FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip setuptools
WORKDIR /src

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./src /src
EXPOSE ${SERVER_PORT}

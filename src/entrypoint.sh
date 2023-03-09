#!/bin/sh

alembic upgrade head
uvicorn --port ${SERVER_PORT} --host 0.0.0.0 --loop uvloop --reload main:app

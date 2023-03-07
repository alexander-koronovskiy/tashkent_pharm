FROM python:3.10-alpine

RUN pip install --upgrade pip setuptools
WORKDIR /src

COPY ./src ./src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE ${SERVER_PORT}
CMD ["entrypoint.sh"]

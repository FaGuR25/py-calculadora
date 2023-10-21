FROM python:3.9.18-slim

ENV TERM xterm

WORKDIR /app

COPY . /app


CMD [ "python", "main.py" ]
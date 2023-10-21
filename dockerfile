FROM python:3.9.18-slim

WORKDIR app

COPY . .


CMD [ "python", "main.py" ]
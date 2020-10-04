FROM python:alpine

COPY . /app
WORKDIR /app

RUN apt-get update -y && apt-get install apt-file -y && apt-file update -y && apt-get install -y python3-dev build-essential


CMD ["python", "main.py"]
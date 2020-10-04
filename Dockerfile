FROM jfloff/alpine-python:3.6-onbuild

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
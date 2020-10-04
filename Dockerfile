FROM jfloff/alpine-python:3.6-onbuild

COPY . /app
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install cython \
    && apk del .build-deps gcc musl-dev

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
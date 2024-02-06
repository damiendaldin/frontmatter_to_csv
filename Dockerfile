FROM python:3.10-alpine

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN apk --no-cache add \
        build-base \
        libffi-dev \
    && pip install pipenv \
    && pipenv install --deploy --ignore-pipfile \
    && apk del build-base libffi-dev \
    && rm -rf /var/cache/apk/*

COPY . /app

ENTRYPOINT ["pipenv", "run", "python", "main.py"]

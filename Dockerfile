FROM python:3.10-slim-bullseye

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . /app

ENTRYPOINT ["pipenv", "run", "python", "main.py"]

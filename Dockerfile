FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.2.2

COPY pyproject.toml /app/
COPY poetry.lock /app/

RUN poetry install

COPY . /app/


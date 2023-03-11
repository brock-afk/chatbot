FROM python:3.11-slim

WORKDIR /app

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry==1.2.2

COPY poetry.lock /app
COPY pyproject.toml /app

RUN poetry install

COPY src /app

RUN poetry install

ENTRYPOINT [ "poetry", "run", "python", "-m", "chatbot" ]

CMD [ "Hello, World!" ]
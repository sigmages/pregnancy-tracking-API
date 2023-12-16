FROM python:3.11-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN mkdir /app
WORKDIR /app

COPY ./app/ /app/
COPY ./pyproject.toml /app/
COPY ./poetry.lock /app/
COPY ./Makefile Makefile

RUN apt-get update
RUN apt-get install make

RUN make poetry/setup
RUN poetry config virtualenvs.create false
RUN make poetry/install-dependencies

CMD gunicorn --bind 0.0.0.0:8000 core.wsgi:application
EXPOSE 8000

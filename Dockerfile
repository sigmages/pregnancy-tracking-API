FROM python:3.11-slim-bullseye

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

RUN mkdir /app
WORKDIR /app

COPY ./app/application application
COPY ./app/core core
COPY ./app/infrastructure infrastructure
COPY ./app/manage.py manage.py
COPY ./pyproject.toml pyproject.toml
COPY ./poetry.lock poetry.lock
COPY ./Makefile Makefile

RUN apt-get update
RUN apt-get install make

RUN make poetry/setup
RUN poetry config virtualenvs.create false
RUN make poetry/install-dependencies

RUN python manage.py collectstatic --noinput

CMD gunicorn --workers 3 --bind 0.0.0.0:8000 --chdir app/ core.wsgi

EXPOSE 8000

# Dockerfile to build dev container
FROM python:3.8-slim

RUN apt-get update -qq && \
    apt-get install --no-install-recommends -yqq git 

RUN pip install poetry==1.5.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache 

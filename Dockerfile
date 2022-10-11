FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN pip install tox

WORKDIR /app

COPY . /app

EXPOSE 443

CMD tox -e api 

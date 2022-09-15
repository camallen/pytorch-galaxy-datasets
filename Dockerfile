FROM python:3.7-slim

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /usr/src/app

RUN apt-get update && apt-get -y upgrade && \
    apt-get install --no-install-recommends -y \
    build-essential \
    git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install dependencies
COPY README.md .
COPY setup.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -e .

# install package code
COPY . .

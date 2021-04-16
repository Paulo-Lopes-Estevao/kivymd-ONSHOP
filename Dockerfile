FROM python:3

LABEL maintainer="https://github.com/Paulo-Lopes-Estevao"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /onshop

WORKDIR /onshop

VOLUME /onshop/

COPY requirements.txt /onshop/

RUN pip install -r requirements.txt || pip3 install -r requirements.txt

COPY . /onshop/

FROM scratch

COPY . /onshop/
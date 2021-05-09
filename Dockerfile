FROM python:3

LABEL maintainer="https://github.com/Paulo-Lopes-Estevao"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /onshop

WORKDIR /onshop

COPY requirements.txt /onshop/

RUN pip install -r requirements.txt

COPY . /onshop/

CMD [ "python", "main.py -m screen:droid2,portrait" ]
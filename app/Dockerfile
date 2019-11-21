# pull official base image
FROM python:3.8.0-alpine

MAINTAINER Vajk Turi (turi.vajk@gmail.com)

# set work directory
WORKDIR /usr/src/app

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

RUN pip install Pillow==6.2.1
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app/




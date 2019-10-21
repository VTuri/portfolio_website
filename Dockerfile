FROM python:3.7

MAINTAINER Vajk Turi (turi.vajk@gmail.com)


RUN mkdir /app
WORKDIR /app

ADD app /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "/app/manage.py", "runserver", "0.0.0.0:8000"]

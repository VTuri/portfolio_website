#!/bin/sh

echo DEBUG=0 >> .env
echo SECRET_KEY=$SECRET_KEY >> .env
echo DJANGO_ALLOWED_HOSTS =$DJANGO_ALLOWED_HOSTS >> .env
echo SQL_ENGINE=django.db.backends.postgresql >> .env
echo SQL_DATABASE=$SQL_DATABASE >> .env
echo SQL_USER=$SQL_USER >> .env
echo SQL_PASSWORD=$SQL_PASSWORD >> .env
echo SQL_HOST=$SQL_HOST >> .env
echo SQL_PORT=$SQL_PORT >> .env
echo DATABASE=postgres >> .env

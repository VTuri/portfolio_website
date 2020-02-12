#!/bin/bash

set -e

cd git

echo "Check if the repo still exists in the folder, clone if it isn't"
DIR="portfolio_website"
STATIC_DIR=""
if [ -d "$DIR" ]; then
  echo "${DIR} already exists."
else
  echo "Cloning repository"
  git clone https://github.com/VTuri/portfolio_website.git
fi

cd ${DIR}

echo "Get the newest version and restart the containers"
git pull
sleep 1
cp /root/static/portfolio_img/* /root/git/portfolio_website/app/contact/static/img
sleep 1
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear;exit
exit
pwd

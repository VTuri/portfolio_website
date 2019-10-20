FROM python:3.7

MAINTAINER Vajk Turi (turi.vajk@gmail.com)

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=hello_django
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/app
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/hello_django

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip



RUN mkdir $DOCKYARD_SRVHOME
WORKDIR $DOCKYARD_SRVHOME

ADD . $DOCKYARD_SRVHOME

RUN pip install -r requirements.txt

EXPOSE 8000

#ENTRYPOINT ["docker-entrypoint.sh"]

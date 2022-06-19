# pull the official docker image
FROM ubuntu:latest
FROM python:3.10.4-buster

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y cron vim
RUN apt-get install gcc libc-dev g++ libffi-dev libxml2 libffi-dev unixodbc-dev -y
RUN pip install -r requirements.txt
# copy project
COPY ./task/task /etc/cron.d/task
COPY . .
# run cron
RUN chmod 0644 /etc/cron.d/task
RUN crontab /etc/cron.d/task
RUN touch /var/log/cron.log
CMD cron
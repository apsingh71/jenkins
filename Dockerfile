FROM python:3

RUN cd /tmp

RUN apt-get update && apt-get install -y python3-pip

RUN pwd

COPY *.py ./tmp/

COPY *.txt ./tmp/

RUN ls -lat

ARG SSH_KEY

ENV SSH_KEY=$SSH_KEY

RUN python hello_world.py "$SSH_KEY"

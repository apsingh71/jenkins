FROM python:3

RUN apt-get update && apt-get install -y python3-pip

RUN pwd

RUN python hello_world.py

FROM python:3

WORKDIR "/tmp"

RUN apt-get update && apt-get install -y python3-pip

RUN pwd

COPY *.py /tmp/

COPY *.txt /tmp/

RUN ls -lat

ARG SSH_KEY

ENV SSH_KEY=$SSH_KEY

#CMD ["python", "hello_world.py", "$SSH_KEY"]

CMD ["python", "countwords.py", "words.txt"]

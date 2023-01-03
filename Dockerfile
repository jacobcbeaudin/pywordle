FROM ubuntu:22.04

WORKDIR /app

RUN apt-get -y update && \
  apt-get -y install python3.10 \
  software-properties-common \
  python3-pip \
  cmake

ADD requirements.txt .

RUN python3 -m pip install -r requirements.txt

RUN rm requirements.txt

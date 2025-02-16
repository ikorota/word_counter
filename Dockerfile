FROM ubuntu:24.04

RUN yes | /usr/bin/unminimize
RUN apt-get update
RUN export DEBIAN_FRONTEND=noninteractive && yes | apt install python3
RUN yes | apt install python3.12-venv
RUN python3 -m venv /opt/word_counter/word_counter
ADD *.* /opt/word_counter
ADD test /opt/word_counter/test
SHELL ["/bin/bash", "-c"]
ENV PATH="/opt/word_counter/word_counter/bin:$PATH"
RUN pip install -r /opt/word_counter/requirements.txt
WORKDIR /opt/word_counter

FROM python:3.7-slim

RUN apt update -y && \
    apt install -y python3-dev net-tools curl && \
    pip3 install --upgrade pip
WORKDIR /opt

COPY ./stinger .
COPY ./configs ./configs

RUN pip3.7 install requirement ./requirements.txt

ENV PYTHONPATH=/opt:$PYTHONPATH
ENV CONFIG_PATH=/opt/configs/

EXPOSE 8080

ENTRYPOINT python3 ./run.py

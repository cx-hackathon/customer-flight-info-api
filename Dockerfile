# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker
FROM tiangolo/uvicorn-gunicorn:python3.10

# upgrade pip to latest (version 20.2.4)
RUN \
pip3 install --upgrade pip

# install required packages
COPY ./app/requirements.txt /app/requirements.txt

RUN \
pip3 install -U -r /app/requirements.txt

# copy app files to "app" directory
COPY ./app /app

# add docker label
ARG TITLE
LABEL org.opencontainers.image.title=$TITLE

ARG BUILD_DATE
LABEL org.opencontainers.image.create=$BUILD_DATE

EXPOSE 80

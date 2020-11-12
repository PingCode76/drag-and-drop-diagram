#!/bin/bash
app="docker-flask.dev"
docker build -t ${app} .
docker run -d \
  --name=${app} \
  -v "$PWD:/app ${app}"


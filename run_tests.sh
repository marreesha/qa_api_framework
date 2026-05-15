#!/bin/bash
set -e

IMAGE_NAME=qa-api-tests

if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
  echo "Image not found. Building..."
  docker build -t $IMAGE_NAME .
fi

docker run --rm --env-file .env \
  -v $(pwd)/allure-results:/app/allure-results \
  $IMAGE_NAME pytest --alluredir=allure-results
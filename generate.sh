#!/bin/bash

VERSION='0.0.1'

while getopts "v:" arg; do
  case $arg in
    v)
      VERSION=$OPTARG
      ;;
  esac
done

swagger-codegen generate -t ./template -l python -i ./res/fingerprint-server-api.yaml -o ./ -c config.json -DpackageVersion=$VERSION

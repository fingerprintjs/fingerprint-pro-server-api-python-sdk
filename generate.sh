#!/bin/bash

VERSION='0.0.2-beta.5'

while getopts "v:" arg; do
  case $arg in
    v)
      VERSION=$OPTARG
      ;;
  esac
done

# jar was downloaded from here https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.34/

java -jar ./bin/swagger-codegen-cli.jar generate -t ./template -l python -i ./res/fingerprint-server-api.yaml -o ./ -c config.json -DpackageVersion=$VERSION

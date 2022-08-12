#!/bin/bash

VERSION='0.0.1'

swagger-codegen generate -t ./template -l python -i ./res/fingerprint-server-api.yaml -o ./ -c config.json -DpackageVersion=$VERSION

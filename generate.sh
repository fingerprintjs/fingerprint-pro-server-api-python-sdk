#!/bin/sh

swagger-codegen generate -t ./template -l python -i https://fingerprintjs.github.io/fingerprint-pro-server-api-openapi/schemes/fingerprint-server-api.yaml -o ./ -c config.json
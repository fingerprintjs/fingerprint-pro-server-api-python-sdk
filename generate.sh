#!/bin/sh

swagger-codegen generate -t ./template -l python -i https://fingerprintjs.github.io/fingerprint-pro-server-api-openapi/schemes/fingerprint-server-api.yaml -o ./ --git-user-id fingerprintjs --git-repo-id fingerprint-pro-server-api-python-sdk -DpackageName=fingerprint_pro_server_api_sdk
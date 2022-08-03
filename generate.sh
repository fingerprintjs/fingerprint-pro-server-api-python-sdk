#!/bin/bash

swagger-codegen generate -t ./template -l python -i https://fingerprintjs.github.io/fingerprint-pro-server-api-openapi/schemes/fingerprint-server-api.yaml -o ./ -c config.json

examplesList=(
  'visits_limit_1.json'
  'visits_limit_500.json'
  'webhook.json'
)

for example in ${examplesList[*]}; do
  curl -o ./test/mocks/"$example" https://fingerprintjs.github.io/fingerprint-pro-server-api-openapi/examples/"$example"
done

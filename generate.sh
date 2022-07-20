#/bin/sh

swagger-codegen generate -t ./template -l python -i ./mock2.yaml -o ./sw_sdk

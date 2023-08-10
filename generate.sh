#!/bin/bash

VERSION='2.5.0.dev3'

while getopts "v:" arg; do
  case $arg in
    v)
      VERSION=$OPTARG
      ;;
  esac
done

# Make prerelease version compatible with PEP 440
if [[ $VERSION =~ (.*-dev\.)([0-9]+) ]]; then
  BASE_VERSION=${BASH_REMATCH[1]}
  DEV_NUMBER=${BASH_REMATCH[2]}
  VERSION="${BASE_VERSION%-dev.}.dev${DEV_NUMBER}"
fi

# jar was downloaded from here https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.34/

rm docs/*
cd fingerprint_pro_server_api_sdk/models
shopt -s extglob
rm !("many_requests_response.py")
cd ../..
java -jar ./bin/swagger-codegen-cli.jar generate -t ./template -l python -i ./res/fingerprint-server-api.yaml -o ./ -c config.json -DpackageVersion=$VERSION

# Ugly fix for codegen problem that I couldn't fix editing template.
# Platform check
platform=$(uname)
(
  # Readme file fix
  replacement=$(printf 'The rawAttributes object follows this general shape: `{ value: any } | { error: { name: string; message: string; } }`\n')
  readme_filename="./docs/RawDeviceAttributesResult.md"
  if [ "$platform" = "Darwin" ]; then
    sed -i '' "s/^Name |.*/${replacement}/" "$readme_filename"
    sed -i '' "/^------------ |/c\\" "$readme_filename"
  else
    sed -i "s/^Name |.*/${replacement}/" "$readme_filename"
    sed -i "/^------------ |/c\\" "$readme_filename"
  fi
)

# Replace version in other files
(
  if [ "$platform" = "Darwin" ]; then
    sed -i '' "s/^VERSION='[^']*'/VERSION='${VERSION}'/" "./generate.sh"
    sed -i '' "s/^VERSION = '[^']*'/VERSION = '${VERSION}'/" "./test/test_fingerprint_api.py"
  else
    sed -i "s/^VERSION='[^']*'/VERSION='${VERSION}'/" "./generate.sh"
    sed -i "s/^VERSION = '[^']*'/VERSION = '${VERSION}'/" "./test/test_fingerprint_api.py"
  fi
)

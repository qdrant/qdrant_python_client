docker run --rm \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    -v "${PWD}:/local" openapitools/openapi-generator-cli:latest generate \
    -i https://raw.githubusercontent.com/qdrant/qdrant/master/openapi/openapi-merged.yaml \
    -g python \
    -o /local/.



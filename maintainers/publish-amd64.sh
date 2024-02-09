#!/usr/bin/bash

VERSION="0.4.0"

cd ..

docker buildx build --platform linux/amd64 -t socraticdevblog/frontmatter_to_csv:amd64-${VERSION} --push .

#!/bin/bash

VERSION="0.4.0"

cd ..

docker buildx build --platform linux/arm64 -t socraticdevblog/frontmatter_to_csv:arm64-${VERSION} --push .

# maintainers - frontmatter_to_csv

## dockerhub

we publish to Dockerhub

[https://hub.docker.com/repository/docker/socraticdevblog/frontmatter_to_csv/general](https://hub.docker.com/repository/docker/socraticdevblog/frontmatter_to_csv/general)

## versionning

SEMVER (MAJOR.MINOR.PATCH)

every build increment will demand to increment the minor version number

unless there is a breaking change

if a bug discovered after a release is fixed, PATCH version number is increased

unless we get paid considerable bribe, we won't retroactively fix bugs in
previous version

### latest version

once a version is deemed stable enough, we will tag it as `latest`

## architectures

- `linux/arm64` images are built on macos, M1 CPU
- `linux/amd64` images are built either on regular gnu/linux machine, or `wsl`
  on Windows
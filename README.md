![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Microsoft Excel readble CSV](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

# metadata_to_csv

simple python script that parses files' frontmatter section and output files' metadata as a machine-readable CSV file

a Frontmatter is a YAML style key-value pair section delimited by triple-dashed-lines above and under:

```yaml
---
date: 2024-02-03
topics:
  - data
  - intelligence
---
```

## Authors

- [@socraticDev](https://github.com/socraticDevBlog/)

## Installation

Install my-project with pipenv

```bash
  pipenv install
```

## Run Locally

start a python shell within your virtual environment

```bash
  pipenv shell
```

execute script

```bash
  python main.py "example_files"
```

## Demo

as long as a frontmatter section exists in a file of any type, **metadata_to_csv** will parse its metadata and print out a CSV file containing the metadata of all files in this directory

### CSV machine readable file generated from files' metadata

```csv
author,country,file_type
Kid Kubernetes,USA,yaml
gunther,germany,python
Jacques Derrida,France,markdown
max,canada,txt
```

### from collection of files in a directory

a python file:

```python
---
author: gunther
country: germany
file_type: python
---

print("hello world")
...
```

a markdown file:

```markdown
---
author: Jacques Derrida
country: France
file_type: markdown
---

# the pharmakon hon hon

## first section

...
```

a yaml file:

```yaml
---
author: Kid Kubernetes
country: USA
file_type: yaml
---
kind: ultraNice
api: basic/v1
grocery:
  - milk
  - bread
  - yogurt
```

a txt file:

```txt
---
author: max
country: canada
file_type: txt
---

abcdefg
```

## Run in Docker container

you don't want to bother setting your local machine up with Python, you can run
the script in a Docker container

1. edit `docker.sh` variables to fit your situation
2. execute script

  ```bash
  chmod +x docker.sh

  ./docker.sh
  ````

3. retrieve your metadata dataset in a csv file in this directory: `metadata.csv`
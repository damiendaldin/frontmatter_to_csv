# metadata_to_csv

will parse any file frontmatter and outpout a CSV containing files metadata

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
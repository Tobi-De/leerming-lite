# leerming

[![falco](https://img.shields.io/badge/built%20with-falco-success)](https://github.com/Tobi-De/falco)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)

[Leerming](github.com/tobi-de/leerming) using sqlite and with no AI features.

## Prerequisites

- `Python 3.11+`
- `hatch 1.9.1+`

## Development

### Create a new virtual environment

```shell
hatch shell
```

### Install pre-commit

```shell
git init && pre-commit install
```

Ensure that the Python version specified in your `.pre-commit-config.yaml` file aligns with the Python version installed on your system.

### Apply migrations

```shell
hatch run migrate
```

### Create a superuser

Follow the tip described [here](https://falco.oluwatobi.dev/guides/tips_and_extra.html#create-superuser-from-environment-variables) and execute the command below to create a superuser.

```shell
python manage.py createsuperuser --no-input
```

### Run the django development server

```shell
falco work
```

## Build binary with shiv

1. Add this config in `pyproject.toml`:

    ```toml
    [tool.hatch.build.targets.sdist]
    only-include = ["leerming", "manage.py"]
    ```

2. Build package with hatch

    ```shell
    hatch build
    ```

3. Add a `main.py` project package to server as entry point:

4. Build app with shiv

    ```shell
    shiv --site-packages dist --compressed \
    -p '/usr/bin/env python3' \
    -o leerming.pyz \
    -e leerming.main:main \
    . -r requirements.txt
    ```

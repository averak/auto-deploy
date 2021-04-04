# auto-deploy

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)

## Requiremenst

- Python ~> 3.8
- pipenv

## Installation

```sh
$ git clone <this repo>
$ cd <this repo>

$ mv sample.env .env
# you need to set access token in .env
$ pipenv install
```

## Usage

See `scripts` section of [Pipfile](./app/Pipfile)

- `pipenv run start`
- `pipenv run format`
- `pipenv run lint`

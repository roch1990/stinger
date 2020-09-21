[![EO principles respected here](https://www.elegantobjects.org/badge.svg)](https://www.elegantobjects.org)
[![We recommend IntelliJ IDEA](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/idea/)

![](https://upload.wikimedia.org/wikipedia/commons/6/66/AH-64D_Apache_Longbow.jpg)

# STINGER
# Table of contents

- [Introduction](#introduction)
    - [What is that](#what-is-that)
    - [Why](#why)
    - [Python versions compability](#python-versions-compability)
- [Use-cases](#use-cases)
    - [Shell](#from-shell)
    - [Pre-commit hook](#add-linter-to-pre-commit-hooks)
- [Some theoretical nuances](#some-theoretical-nuances)
    - [Why naive](#why-naive)
- [Development](#development)
    - [Testing](#testing)
    - [Contributing](#contributing)
        - [Commit naming conventions](#commit-naming-conventions)
        - [Pull-request naming conventions](#pull-request-naming-conventions)
- [License](./LICENSE.txt)

# Introduction
## What is that?

Simple ping-tool for your web-sites.

You can setup your endpoints by addition of json-like configs.
And that is all :)

## Why?

For example, you need to monitor SLA at non-production servers and check your calculate-formulas/alerting-rules.
For that - you need a small request payload into your services.
And you think, that load-testing tools are over-engineering for that case.

Okay, you can write a small json-config (you can see example below), add it to 'Stinger'.

Hurray! It works! Stinger pings your server by rules with specified frequency.

# How I can add new config

In project root directory you should see directory 'configs'.
You can add your json-configs into.

Configuration example:

```json
{
  "uri": "https://www.example.com",                                         # http/https addr
  "port": 443,                                                              # port
  "name": "health",                                                         # rule name (need for operations with ping process)
  "route": "/ping",                                                         # route
  "method": "POST",                                                         # method type
  "timeout": 5,                                                             # timeout between requests
  "headers": {"Content-Type": "application/json"},                          # request header
  "payload": {"jsonrpc": "2.0", "method": "ping", "params": [], "id": 1}    # payload
}
}
```

json-schema:

```json
{
    "type": "object",
    "properties": {
        "uri": {
            "type": "string",
            "format": "uri"
        },
        "port": {
            "type": "integer",
            "minimum": 0,
            "maximum": 65535,
        },
        "name": {
            "type": "string",
            "minLength": 2,
            "maxLength": 20
        },
        "route": {
            "type": "string",
            "pattern": "^\/[a-zA-Zа-яА-Я0-9 _\-\/]{1,}$"
        },
        "method": {
            "type": "string",
            "pattern": "^(GET|POST|PATCH|PUT|DELETE)$"
        },
        "timeout": {
            "type": "integer",
            "minimum": 2,
            "maximum": 600
        },
        "headers": {
            "type": "object"
        },
        "payload": {
            "type": "object"
        }
    },
    "required": [
        "uri",
        "port",
        "name",
        "route",
        "method",
        "timeout"
    ]
}
```

# Ping process operation

You can check ping process status, by call api method:

```bash
/status
```

You can restart your ping-process by call api method (name - it's `name` field from json-config):

```bash
/restart/{name}
```

# Development

## Pre-requisite

After you clone repo:
- create virtual env

`python3 -m venv /path/to/new/virtual/environment`

- install requirements

`pip3 install - r ./stinger/requirements.txt`

- install pre-commit hooks

`pre-commit install`

- setup PYTHONPATH

`export PYTHONPATH=$PWD/stinger`

And then feel free to make a changes.

## Testing

You can start local tests:

```bash
make tests
```

this instruction starts - unit, mutual and security tests.

Yuo can tests pre-commit integration:

```bash
make local-run
```

Show results of mutual tests:

```bash
mutmut results
```

Show result of concrete mutual tests:

```bash
mutmut show <test_id:int>
```

## Contributing

Easiest way is:
- fork
- make changes at your branch
- commit and create PR to dev branch of this repo

If all check would be passed - I check your changes so fast, as i can.

P.S.: falling of mutual tests - is normal now (in development, as you remember)

### Commit naming conventions

Every commit should start with keyword with colon:
- `feature:` (if you add new functionality)
- `fix:` (if you fix bug or invalid behaviour)
- `chore:` (if you fix something, that you were not going to fix)

Then, after keyword you should shortly describe your changes:
`feature: add sec tests step to travis`

### Pull request naming conventions

Every pull request to dev should start with keyword `pr-dev` and issue number:
`pr-dev: 123`

Every pull request to master should start with keyword `pr` and issue number:
`pr: 123`

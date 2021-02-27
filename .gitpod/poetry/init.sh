#!/usr/bin/env bash

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
poetry completions bash > /etc/bash_completion.d/poetry.bash-completion

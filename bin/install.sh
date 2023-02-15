#!/usr/bin/env bash

set -ex

python3 -m venv venv

# shellcheck source=./venv/bin/activate
source "./venv/bin/activate"
cp .env{.example,}
pip install -r requirements.txt
deactivate

(cd ui && yarn install)
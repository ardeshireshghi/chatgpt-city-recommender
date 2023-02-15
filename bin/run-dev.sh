#!/usr/bin/env bash

set -ex

# shellcheck source=./venv/bin/activate
source "./venv/bin/activate"

flask --app recommender.app run
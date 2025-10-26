#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -o errexit

# Upgrade pip (using python3 module execution)
python3 -m pip install --upgrade pip

# Install dependencies (using python3 module execution)
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear
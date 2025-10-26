#!/bin/bash

# Exit on error
set -o errexit

# Upgrade pip (using python3 module execution)
python3 -m pip install --upgrade pip

# Install dependencies (using python3 module execution)
python3 -m pip install -r requirements.txt

# Collect static files into the directory specified by STATIC_ROOT (which is 'public')
python3 manage.py collectstatic --noinput --clear
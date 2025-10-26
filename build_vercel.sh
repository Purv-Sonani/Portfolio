#!/bin/bash

# Exit on error
set -o errexit

# Upgrade pip (Good practice)
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

# Rename the output directory to match vercel.json config
mv staticfiles staticfiles_build
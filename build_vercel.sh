#!/bin/bash

# Exit on error
set -o errexit

# Install dependencies (Vercel might do this automatically, but explicit is safer)
pip install -r requirements.txt

# Collect static files into the 'staticfiles' directory
python3 manage.py collectstatic --noinput --clear
#!/bin/bash

# Exit on error
set -o errexit

# Collect static files (make sure python3 is correct)
python3 manage.py collectstatic --noinput --clear
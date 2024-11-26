#!/bin/bash

# Exit on error
set -e

# Debugging: Print Python version
echo "Python version: $(python3.9 --version)"

# Ensure pip is available
echo "Ensuring pip is installed..."
python3.9 -m ensurepip --upgrade

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear -c

# Apply migrations (optional)
echo "Applying database migrations..."
python manage.py migrate

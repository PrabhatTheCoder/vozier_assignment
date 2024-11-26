#!/bin/bash

# Exit on error
set -e

# Debugging: Print the working directory
echo "Current directory: $(pwd)"

# Ensure pip is installed
echo "Ensuring pip is installed..."
python3.9 -m ensurepip --upgrade  # Install pip if not available

# Ensure pip is accessible
echo "Ensuring pip is available on PATH..."
python3.9 -m pip --version

# Install dependencies from requirements.txt
echo "Installing dependencies..."
python3.9 -m pip install --upgrade pip  # Upgrade pip to the latest version
python3.9 -m pip install -r requirements.txt  # Install all dependencies from requirements.txt

# Verify Django installation (optional)
echo "Verifying Django installation..."
python3.9 -c "import django; print(django.get_version())"

# Collect static files
echo "Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear -c

# Apply migrations (optional)
echo "Applying database migrations..."
python3.9 manage.py migrate


mkdir -p dist
touch dist/placeholder.txt

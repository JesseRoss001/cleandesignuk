#!/bin/bash
set -e

# Wait for the database to be ready (optional, implement your own logic or use a tool like wait-for-it, dockerize, or similar)
# Example: wait-for-it db:5432 --timeout=30

# Activate the virtual environment
source venv/bin/activate

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear

# Start Gunicorn
exec "$@"

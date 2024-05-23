#!/bin/bash

# Activate the virtual environment
source /workspace/venv/bin/activate

# Run migrations (if needed)
python manage.py migrate

# Install dependencies
pip install -r requirements.txt

# Start the Django development server
nohup python manage.py runserver 0.0.0.0:8000 &

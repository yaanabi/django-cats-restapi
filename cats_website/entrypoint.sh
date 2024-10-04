#!/bin/sh

# Making migartions
python manage.py makemigrations
python manage.py migrate --noinput

# Load initial data
echo "Loading initial data..."
python manage.py loaddata data_populate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn server
echo "Starting Gunicorn server..."
exec gunicorn cats_website.wsgi:application --bind 0.0.0.0:8000 --reload
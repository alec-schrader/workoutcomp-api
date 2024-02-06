#!/bin/sh

# Change to the app directory
cd workoutcomp_api

# Apply database migrations
echo "Applying database migrations"
python manage.py makemigrations
python manage.py migrate --noinput

# Start the server using gunicorn
echo "Starting the server"
gunicorn workoutcomp_api.wsgi:application --bind 0.0.0.0:8000
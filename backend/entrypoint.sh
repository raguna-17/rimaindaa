#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating demo user if not exists..."
python backend/init_demo_user.py || echo "Demo user script skipped"

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn pro.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3

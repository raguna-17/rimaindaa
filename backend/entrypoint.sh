#!/bin/sh
set -e

python manage.py migrate --noinput
python init_demo_user.py       # ← backend直下ならパスはこれ
python manage.py collectstatic --noinput
gunicorn pro.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3

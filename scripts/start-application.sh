#!/usr/bin/env bash

set -e

python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear
gunicorn py_card.wsgi -b 0.0.0.0:${DJANGO_BIND_PORT:-8000}

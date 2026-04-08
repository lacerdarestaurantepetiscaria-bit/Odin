#!/usr/bin/env bash
set -o errexit
pip install -r requirements.txt
if [ -f requirements-prod.txt ]; then
  pip install -r requirements-prod.txt
fi
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py bootstrap_admin

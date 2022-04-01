#! /usr/bin/env bash
set -e

# Let the DB start
python /code/app/pre_start.py

# Run migrations
alembic upgrade head

# start app
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

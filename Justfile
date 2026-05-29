# Justfile for Kwiek Energie project
# Install just: https://github.com/casey/just

# Show available recipes
default:
    @just --list

# Install all Python + Node dependencies
install:
    uv sync --all-extras --all-packages --group dev
    pnpm install

# Git actions
sandbox:
    git checkout sandbox
    git pull

# Run tests
test:
    uv run pytest

# ---------------------------------------------------------------------------
# Format
# ---------------------------------------------------------------------------

# Auto-format all code
format: format-backend

format-backend:
    uv run ruff format apps/backend/src apps/backend/tests
    uv run ruff check --fix apps/backend/src apps/backend/tests

# Auto-format all packages
format-packages:
    uv run ruff format packages/*/src packages/*/tests
    uv run ruff check --fix packages/*/src packages/*/tests

# ---------------------------------------------------------------------------
# Linting
# ---------------------------------------------------------------------------

# Run all linters
lint: lint-backend lint-frontend

# Run ruff check + format check + mypy
lint-backend:
    uv run ruff check apps/backend/src apps/backend/tests
    uv run ruff format --check apps/backend/src apps/backend/tests
    uv run mypy apps/backend/src

# Run eslint + tsc
lint-frontend:
    pnpm --filter frontend lint
    pnpm --filter frontend type-check

# ---------------------------------------------------------------------------
# Local development
# ---------------------------------------------------------------------------

dev-backend:
    uv run --package backend dev

dev-dashboard:
    uv run dashboard-dev

dev-celery:
    uv run --package backend celery -A backend.jobs.celery worker -B --loglevel=info

dev-flower:
    uv run --package backend celery -A backend.jobs.celery flower &
    open http://localhost:5555

dev-web:
    pnpm --filter reminder-ai dev

# ---------------------------------------------------------------------------
# DB
# ---------------------------------------------------------------------------

# Delete the latest alembic revision and regenerate it via autogenerate, keeping the same message
regenerate-revision:
    #!/usr/bin/env bash
    set -euo pipefail
    file=$(ls packages/db/alembic/versions/ | grep -v __pycache__ | sort | tail -1)
    filepath="packages/db/alembic/versions/$file"
    name="${file%.py}"
    after_dash="${name##*-}"
    message="${after_dash#*_}"
    echo "Deleting: $file (message: $message)"
    rm "$filepath"
    uv run --package db alembic --config packages/db/alembic.ini revision --autogenerate -m "$message"

# Show help
help:
    @just --list

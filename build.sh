#!/usr/bin/env bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv run main.py
npm run sources
npm run build:strict

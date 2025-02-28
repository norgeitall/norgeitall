#!/usr/bin/env bash
pip install --upgrade uv
uv run main.py
npm run sources
npm run build

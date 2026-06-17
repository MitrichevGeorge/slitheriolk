#!/bin/bash

if command -v python3.13 &> /dev/null; then
    echo "Python 3.13 found! Using it..."
    PYTHON_BIN="python3.13"
elif command -v python3 &> /dev/null; then
    echo "Python 3.13 found! Using it..."
    PYTHON_BIN="python3"
else
    echo "Error: Neither python3.13 nor python3 could be found." >&2
    exit 1
fi

$PYTHON_BIN -m venv .env
source .env/bin/activate
pip install -r requirements.txt
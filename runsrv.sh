#!/bin/bash

source .env/bin/activate
uvicorn server:app --port 90801 --reload
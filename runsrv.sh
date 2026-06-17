#!/bin/bash

source .env/bin/activate
uvicorn srv.main:app --port 90801 --reload
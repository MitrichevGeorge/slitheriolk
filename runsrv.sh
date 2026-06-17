#!/bin/bash

source .env/bin/activate
cd srv
uvicorn main:app --port 90801 --reload
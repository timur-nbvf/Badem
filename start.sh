#!/bin/bash
uvicorn bot:app --host=0.0.0.0 --port=8000 &
python3 bot.py
#!/bin/bash
uvicorn Bot:app --host=0.0.0.0 --port=8000 &
python3 Bot.py

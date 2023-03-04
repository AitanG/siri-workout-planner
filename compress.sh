#! /bin/sh

zip -r archive.zip main.py requirements.txt store.py workout_planner "$@" -x '**/.*' -x '**/__MACOSX'

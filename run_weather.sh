#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: ./run_weather.sh <City>"
  exit 1
fi

CITY="$1"
docker exec -it ovos_cli bash -c "source ~/.venv/bin/activate && cd /home/ovos/skills/skill-weather-owm && python3 test_weather.py \"$CITY\""


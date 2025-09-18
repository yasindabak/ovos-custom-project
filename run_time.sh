#!/bin/bash

docker exec -it ovos_cli bash -c "source ~/.venv/bin/activate && cd /home/ovos/skills/skill-weather-owm && python3 test_time.py"


#!/bin/sh
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 python|octave|ir TOKEN" >&2
  exit 1
fi
docker run --rm --memory=4g --cpus=2 --volume="$(pwd)/work:/home/jovyan/work:rw" stem-bot:$1 python bot.py $1 $2

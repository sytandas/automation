#!/usr/bin/env bash

./proto.py

while [ ! -f /Users/sayantandas/fun/automation/track_debugger.csv ]
do
  touch track_debugger.csv
done

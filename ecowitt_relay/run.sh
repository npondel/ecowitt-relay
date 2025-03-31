#!/bin/bash

export PWSWEATHER_STATION_ID=$(jq -r .pws_id /data/options.json)
export PWSWEATHER_API_KEY=$(jq -r .pws_key /data/options.json)
export RELAY_PORT=$(jq -r .relay_port /data/options.json)

/usr/local/bin/python /app/ecowitt_relay.py
#!/bin/bash

export PWSWEATHER_STATION_ID=$(jq -r .pws_id /data/options.json)
export PWSWEATHER_API_KEY=$(jq -r .pws_key /data/options.json)
export RELAY_PORT=$(jq -r .relay_port /data/options.json)
export HA_WEBHOOK_PATH=$(jq -r .ha_webhook_path /data/options.json)
export HA_WEBHOOK_HOST=$(jq -r .ha_webhook_host /data/options.json)
export HA_WEBHOOK_PORT=$(jq -r .ha_webhook_port /data/options.json)

/usr/local/bin/python -u /app/ecowitt_relay.py

# Ecowitt Relay Home Assistant Add-on
Ecowitt only supports a single custom endpoint to send data to.  This add-on allows sending to HA and PWSweather at the same time, via a simple Flask relay server.

## Configuration

| Option              | Description                                                  |
|---------------------|--------------------------------------------------------------|
| `pws_id`            | Your PWSweather station ID                                   |
| `pws_key`           | Your PWSweather API key                                      |
| `relay_port`        | The port this add-on listens on for incoming Ecowitt data    |
| `ha_webhook_path`   | The full webhook path (e.g., `/api/webhook/abcd1234...`)     |
| `ha_webhook_host`   | Hostname of Home Assistant instance (default: `homeassistant`)|
| `ha_webhook_port`   | Port of the Home Assistant instance (default: `8123`)        |


## Usage

1. Add this repository to Home Assistant.  (Add-on Store > three-dot menu > Repositories)
2. Install the "Ecowitt Relay" add-on.
3. Configure the relay add-on with the URL, port, and host provided in the EcoWitt configuration.
4. Set the Ecowitt console to upload to `http://<HA_IP>:5000/weather`.  Change port if you changed it in the configuration.

If all is going well, your EcoWitt should be sending data to port 5000, where this relay add-on picks up the data and relays it to HA's webhook url for EcoWitt, and the PWS weather API.
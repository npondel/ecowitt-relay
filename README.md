# Ecowitt Relay Home Assistant Add-on

This add-on receives  data from the Ecowitt weather station and forwards it to:

- Home Assistant (via the Ecowitt integration)
- PWSweather

## Configuration

| Option       | Description                        |
|--------------|------------------------------------|
| `pws_id`     | Your PWSweather station ID         |
| `pws_key`    | Your PWSweather API key            |
| `relay_port` | Port the add-on listens on (default: 5000) |

## Usage

1. Add this repository to Home Assistant.  (Add-on Store > three-dot menu > Repositories)
2. Install the "Ecowitt Relay" add-on.
3. Set your Ecowitt console to upload to `http://<HA_IP>:5000/weather`.
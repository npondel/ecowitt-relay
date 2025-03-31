# Ecowitt Relay Home Assistant Add-on
Ecowitt only supports a single custom endpoint to send data to.  This add-on allows sending to HA and PWSweather at the same time, via a simple Flask relay server.

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
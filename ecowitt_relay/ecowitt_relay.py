import os
from flask import Flask, request
import requests

# Load env variables
HA_WEBHOOK_PATH = os.getenv("HA_WEBHOOK_PATH")
HA_WEBHOOK_HOST = os.getenv("HA_WEBHOOK_HOST", "homeassistant")
HA_WEBHOOK_PORT = os.getenv("HA_WEBHOOK_PORT", "8123")

PWS_ID = os.getenv("PWSWEATHER_STATION_ID")
PWS_KEY = os.getenv("PWSWEATHER_API_KEY")
PORT = int(os.getenv("RELAY_PORT") or 5000)

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def receive_data():
    data = request.form.to_dict()
    print("Received data:", data)

    # === Forward to Home Assistant Webhook ===
    try:
        if HA_WEBHOOK_PATH:
            ha_url = f"http://{HA_WEBHOOK_HOST}:{HA_WEBHOOK_PORT}{HA_WEBHOOK_PATH}"
            response = requests.post(ha_url, data=data)
            print(f"Forwarded to Home Assistant Webhook: {response.status_code}")
        else:
            print("HA Webhook path not set — skipping HA forward.")
    except Exception as e:
        print("HA Forward Error:", e)

    # === Forward to PWSweather ===
    try:
        if PWS_ID and PWS_KEY:
            # Use all incoming parameters:
            pws_payload = data.copy()
            # Remove device-provided PASSKEY if it exists:
            pws_payload.pop('PASSKEY', None)
            # Override with your PWS credentials and add required action:
            pws_payload.update({
                'ID': PWS_ID,
                'PASSWORD': PWS_KEY,
                'action': 'updateraw'
            })
            # Log the final URL with all parameters:
            final_url = requests.Request('GET', 'http://pwsweather.com/pwsupdate/pwsupdate.php', params=pws_payload).prepare().url
            print("Final PWS URL:", final_url)
            response = requests.get('http://pwsweather.com/pwsupdate/pwsupdate.php', params=pws_payload)
            print("Forwarded to PWSweather. Response:", response.text)
        else:
            print("PWS credentials not set — skipping.")
    except Exception as e:
        print("PWS Forward Error:", e)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

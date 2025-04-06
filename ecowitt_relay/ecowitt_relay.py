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
    print("App update: 4-5-25")
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
            pws_payload = {
                'ID': PWS_ID,
                'PASSWORD': PWS_KEY,
                'dateutc': 'now',
                'winddir': data.get('winddir'),
                'windspeedmph': data.get('windspeedmph'),
                'windgustmph': data.get('windgustmph'),
                'humidity': data.get('humidity'),
                'tempf': data.get('tempf'),
                'baromrelin': data.get('baromrelin'),
                'baromabsin': data.get('baromabsin'),
                'rainin': data.get('rainin'),
                'dailyrainin': data.get('dailyrainin'),
                'maxdailygust': data.get('maxdailygust'),
                'solarradiation': data.get('solarradiation'),
                'uv': data.get('uv'),
                'action': 'updateraw',
            }
            requests.get('https://pwsupdate.pwsweather.com/api/v1/submitwx', params=pws_payload)
            print("Forwarded to PWSweather.")
        else:
            print("PWS credentials not set — skipping.")
    except Exception as e:
        print("PWS Forward Error:", e)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

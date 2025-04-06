import os
from flask import Flask, request
import requests

# Load environment variables
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
    
    ha_success = True
    pws_success = True

    # === Forward to Home Assistant Webhook ===
    try:
        if HA_WEBHOOK_PATH:
            ha_url = f"http://{HA_WEBHOOK_HOST}:{HA_WEBHOOK_PORT}{HA_WEBHOOK_PATH}"
            ha_response = requests.post(ha_url, data=data)
            if ha_response.status_code != 200:
                ha_success = False
                print(f"HA Forward Error: Non-200 status code {ha_response.status_code}")
            else:
                print(f"Forwarded to Home Assistant Webhook: {ha_response.status_code}")
        else:
            print("HA Webhook path not set — skipping HA forward.")
    except Exception as e:
        ha_success = False
        print("HA Forward Exception:", e)

    # === Forward to PWS API using Weather Underground formatting ===
    try:
        if PWS_ID and PWS_KEY:
            # Map Ecowitt parameters to Weather Underground format.
            pws_payload = {
                'ID': PWS_ID,
                'PASSWORD': PWS_KEY,
                'action': 'updateraw',
                'dateutc': data.get('dateutc', 'now'),
                'tempf': data.get('tempf'),
                'humidity': data.get('humidity'),
                'winddir': data.get('winddir'),
                'windspeedmph': data.get('windspeedmph'),
                'windgustmph': data.get('windgustmph'),
                'baromrelin': data.get('baromrelin'),
                'baromabsin': data.get('baromabsin'),
                'rainin': data.get('hrain_piezo'),
                'dailyrainin': data.get('drain_piezo'),
                'maxdailygust': data.get('maxdailygust'),
                'solarradiation': data.get('solarradiation'),
                'uv': data.get('uv'),
                'indoortempf': data.get('tempinf'),
                'indoorhumidity': data.get('humidityin'),
            }

            pws_response = requests.get('http://pwsweather.com/pwsupdate/pwsupdate.php', params=pws_payload)
            # Check if the response text contains "error" anywhere
            if "error" in pws_response.text.lower():
                pws_success = False
                print("PWS API returned error response:", pws_response.text)
            else:
                print("Forwarded to PWS API successfully.")
        else:
            print("PWS credentials not set — skipping.")
    except Exception as e:
        pws_success = False
        print("PWS API Forward Exception:", e)

    # Only log full received data if either forward failed
    if not ha_success or not pws_success:
        print("Full received data:", data)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)

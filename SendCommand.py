import requests
import json
import random

def send_command():
    url = "https://discord.com/api/v10/interactions"
    headers = {
        "Authorization": "DISCORD TOKEN",
        "Content-Type": "application/json"
    }

    payload = {
    "type": "2",
    "application_id": "1395493912709304381",
    "guild_id": "1283914146387329067",
    "channel_id": "1395506062475395303",
    "session_id": "07007a9477e2cbe14d0654f62f68be9e",
    "data": {
        "id": "1397477096284229669",
        "version": "1400483405560549440",
        "name": "ping",
        "options": []
    },
        "nonce": str(random.randint(10**18, 10**19 - 1)),
        "analytics_location": "slash_ui",
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.status_code)

send_command()
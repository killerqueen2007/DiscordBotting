import requests
import json
import random

def send_command():
    url = "https://discord.com/api/v10/interactions"
    headers = {
        "Authorization": "DISCORD TOKEN",
        "Content-Type": "application/json"
    }

    payload = {}

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(response.status_code)

send_command()

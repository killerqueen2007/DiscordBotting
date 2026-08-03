import requests
import json
import random

Guild_ID = ""
User_ID= ""

def send_command():
    url = f"https://discord.com/api/v9/guilds/{Guild_ID}/members/{User_ID}"
    headers = {
        "Authorization": "DISCORD TOKEN",
        "Content-Type": "application/json"
    }

    response = requests.delete(url, headers=headers)
    print(response.status_code)

send_command()

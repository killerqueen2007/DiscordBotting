import requests

TOKEN = "DISCORD TOKEN"

r = requests.post(
    "https://discord.com/api/v9/users/@me/invites",
    headers={"Authorization": TOKEN},
    json={}
)

data = r.json()
print(f"https://discord.gg/{data['code']}")
print(f"Uses: {data['uses']}/{data['max_uses']}")
print(f"Expires: {data['expires_at']}")
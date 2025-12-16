import requests

def send_message():
    url = "Your url" # The channel ID you want to send the message in
    headers = {
        "Authorization": "DISCORD TOKEN",
        "Content-Type": "application/json"
    }

    payload = '{"content":"Your message here"}'

    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)

send_message()
import requests

uuid = '<chatbot-uuid>'
url = f'https://app.gpt-trainer.com/api/v1/chatbot/{uuid}/data-source/url'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer <token>'
}

data = {
    "url": "string",
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print("Request failed with status code:", response.status_code)
    print(response.text)

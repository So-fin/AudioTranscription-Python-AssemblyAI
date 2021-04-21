import requests

endpoint = "https://api.assemblyai.com/v2/transcript"

json = {
  "audio_url": "https://cdn.assemblyai.com/upload/0003237d-cd8e-458d-ad36-29ea651c43e6"
}

headers = {
    "authorization": "6a90e0b7b4474918bcb47be82066b350",
    "content-type": "application/json"
}

response = requests.post(endpoint, json=json, headers=headers)

print(response.json())

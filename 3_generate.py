import requests

endpoint = "https://api.assemblyai.com/v2/transcript/8lo7amis4-3ecb-4d9b-b3a7-647229dbb217"

headers = {
    "authorization": "6a90e0b7b4474918bcb47be82066b350",
}

response = requests.get(endpoint, headers=headers)

print(response.json())

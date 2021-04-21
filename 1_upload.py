import sys
import time
import requests

filename = "C:/Users/Admin/Desktop/Sofin/MicaProject/audio.mp3"
 
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data
 
headers = {'authorization': "6a90e0b7b4474918bcb47be82066b350"}
response = requests.post('https://api.assemblyai.com/v2/upload',
                         headers=headers,
                         data=read_file(filename))

print(response.json())

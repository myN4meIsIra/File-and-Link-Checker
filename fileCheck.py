import requests

from api_keys import virus_total_api_key

url = "https://www.virustotal.com/api/v3/files"

headers = {
    "X-Apikey": virus_total_api_key,
    "accept": "application/json",
    "content-type": "multipart/form-data"
}

response = requests.post(url, headers=headers)

print(response.text)
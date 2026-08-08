import requests

from api_keys import virus_total_api_key

url = "https://google.com"


headers = {
    "X-Apikey": virus_total_api_key,
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
}

response = requests.post(url, headers=headers)

print(response.text)
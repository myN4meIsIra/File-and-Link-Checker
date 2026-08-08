import requests

url = "https://www.virustotal.com/api/v3/urls/id"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)
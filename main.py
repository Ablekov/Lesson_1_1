import requests
import json

url = 'https://www.cbr-xml-daily_json.js'
response = requests.get(url)
print(response)

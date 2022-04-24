import requests
import json

url = "https://restcountries.com/v3.1/name/jamaica"

r = requests.get(url)

data = r.json()
pretty_data = json.dumps(data, indent=4)

print(pretty_data)


import json, requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=1ccc384606a371dcdd78875e7b6174e3'
site = requests.get(url)
info = json.loads(site.text)
print(f"Temperature is {info['main']['temp']}")

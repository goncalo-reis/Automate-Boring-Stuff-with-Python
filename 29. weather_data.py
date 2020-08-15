import json, requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=********'
site = requests.get(url)
info = json.loads(site.text)
print(f"Temperature is {info['main']['temp']}")

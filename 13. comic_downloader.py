import requests

response = requests.get('https://imgs.xkcd.com/comics/python.png')
file = open('comic.png', 'wb')
file.write(response.content)

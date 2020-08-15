import requests
import bs4


res = requests.get('https://www.yahoo.com/news/')
res.raise_for_status()

links = bs4.BeautifulSoup(res.text, 'html.parser').select('a')

for link in links:
    link = link.get('href')
    try:
        res = requests.get(link)
        if res.status_code == 404:
            print('404 for: ' + link)
        else:
            print('Working link: ' + link)
    except requests.exceptions.MissingSchema:
        continue

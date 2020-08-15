 #! python3
   # threadedDownloadXkcd.py - Downloads XKCD comics using multiple threads.

import os, threading
from requests_html import HTMLSession

def downloadXkcd(start_comic, end_comic):
   for url_number in range(start_comic, end_comic):
       print(f'{url_number}')
       r = HTMLSession().get(f'https://xkcd.com/{url_number}')
       r.raise_for_status()
       comic = r.html.find('#comic img', first=True)
       if comic == []:
           print('Could not find comic image.')
       else:
           comic_url = comic.attrs['src']
           #print(f'Downloading image {comic_url}...')
           r = HTMLSession().get('https:' + comic_url)
           r.raise_for_status()
           with open(os.path.join('D:\\Ambiente de Trabalho\\pasta', os.path.basename(comic_url)), 'wb') as image_file:
                 image_file.write(r.content)

downloadThreads = []             
for i in range(0, 25, 5):
    start = i
    end = i + 5
    if start == 0:
        start = 1
    if end == 25:
        end += 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
    
for downloadThread in downloadThreads:
    downloadThread.join()
print('done!')

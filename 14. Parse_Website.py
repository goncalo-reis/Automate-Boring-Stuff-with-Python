from requests_html import HTMLSession

response = HTMLSession().get('https://coreyms.com/')

articles = response.html.find('article')
for article in articles:
        headline = article.find('.entry-title-link', first=True).text
        print(headline)
        print()
        
        summary = article.find('.entry-content p', first=True).text
        print(summary)
        print()
        
        try:
            video_code = article.find('.embed-youtube iframe', first=True).attrs['src']
            video_code = video_code.split('/')[4]
            video_code = video_code.split('?')[0]
            video_url = f'https://www.youtube.com/watch?v={video_code}'
            print(video_url)
            print()
            print()
        except:
            print('No video.')
            print()
            print()



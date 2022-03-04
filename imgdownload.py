import cfscrape
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
import sys

headers = {'User Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 [ip:87.8.135.245]'}

def download(url, path):
    scraper = cfscrape.CloudflareScraper()
    req = scraper.get(url, headers=headers)

    bs = BeautifulSoup(req.text, 'html.parser')
    imgs = bs.find_all('img')

    folder = os.path.join(os.getcwd(), path)

    try:
        os.mkdir(folder)
    except:
        pass

    os.chdir(folder)

    name = 0
    for img in imgs:
        src = 'http://' + urlparse(url).netloc + '/' + img['src']
        print(src)
        with open(str(name) + '.jpg', 'wb') as f:
            scrape = cfscrape.CloudflareScraper()
            i = scrape.get(src, headers=headers)
            f.write(i.content)
            print('Downloading: ' + img['src'] + '...')
            name += 1

if __name__ == "__main__":
    download(str(sys.argv[1]), str(sys.argv[2]))

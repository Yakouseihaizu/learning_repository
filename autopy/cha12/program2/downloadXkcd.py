
# downloadXkcd.py - Downloads every single XKCD comic.

import requests,bs4,os

url = 'https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    # TODO: Download the page
    print(f'Download page {url}...')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    # TODO: Find the URL of the comic image
    comicElem = soup.select('div[id="comic"] > img')
    if len(comicElem) == 0:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    # TODO: save the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(10_000):
            imageFile.write(chunk)
        imageFile.close()
    # TODO: Get the Prev button's url
    url = 'https://xkcd.com' + soup.select('a[rel="prev"]')[0].get('href')

print('Done')
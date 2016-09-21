from bs4 import BeautifulSoup
import urllib2

BASE_URL = 'http://www.azlyrics.com/'
a_z = list(map(chr, range(97, 123)))

for letter in a_z:
  with open('data/'+letter+'.txt') as f:
    url = BASE_URL + letter + '.html'
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    # Scrap the artists for a given letter and get their URLs
    with open('data/' + letter + '.txt', 'wb') as w:
      for column in soup.findAll('div', {'class': 'artist-col'}):
        for link in column.findAll('a'):
          w.write(link['href'] + '\n')

from bs4 import BeautifulSoup
import urllib2
import time
import random

BASE_URL = 'http://www.azlyrics.com/'
a_z = list(map(chr, range(97, 123)))

def download_songs(url):
  time.sleep(random.random() * 0.5)
  try:
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')

    # Get the artist name
    artist_name = soup.findAll('h1')[0].get_text()[:-7].lower().replace(' ', '_')

    # Store all songs for a given artist
    with open('artist_data/'+artist_name+'.txt', 'wb') as w:
      for song in soup.findAll('a', {'target': '_blank'}):
        if 'lyrics/' in song['href']:
          song_url = song['href'][1:].strip()
          w.write(song_url + '\n')
  except urllib2.HTTPError:
    print '404 not found'

completed_artists = open('completed_artists.txt', 'r').read().strip().split('\n')

with open('hand_picked.txt', 'r') as f:
  artists = f.read().split('\n')
  random.shuffle(artists)
  with open('completed_artists.txt', 'a') as w:
    for extension in artists:
      url = BASE_URL + extension.strip()
      if url not in completed_artists:
        print url
        download_songs(url)
        w.write(url + '\n')

print 'Complete'
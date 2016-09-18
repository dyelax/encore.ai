from bs4 import BeautifulSoup
import urllib2
import os
from random import random
import time

BASE_URL = 'http://www.azlyrics.com/'


def download_lyrics(artist, url):
  print url
  time.sleep(random() + 2)
  page = urllib2.urlopen(url).read()
  soup = BeautifulSoup(page, 'html.parser')

  # Get the song title
  song_title = soup.find('title').get_text().split(' - ')[1].lower().replace('/', ' ').replace(' ', '_')

  # Get the lyrics div
  lyrics = soup.findAll('div', {'class': ''})

  for i in lyrics:
    lyrics = i.get_text().strip()
    if len(lyrics) > 10:
      with open('artists/' + artist + '/' + song_title + '.txt', 'wb') as w:
        cleaned_lyrics = lyrics.replace('\r\n', ' *BREAK* ').replace('\n', ' *BREAK* ').replace('  ', ' ')
        w.write(cleaned_lyrics.encode('utf-8'))

def download_all_lyrics(artist):
  if not os.path.exists('artists/'+artist):
    os.mkdir('artists/'+artist)

  with open('artist_data/'+artist+'.txt', 'r') as songs:
    for song in songs.readlines():
      url = BASE_URL + song[2:].strip()
      download_lyrics(artist, url)


download_all_lyrics('taylor_swift')
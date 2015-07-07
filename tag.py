from __future__ import print_function

__author__ = 'sachin'
from bs4 import BeautifulSoup
import urllib2

def get_info(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    album_name = soup.find(class_='track-albumname').string
    track_name = soup.find(class_='sngandalbum').contents[1].string
    artist_arr = []
    artists = soup.find(class_='artist').contents[1].contents
    for artist_tag in artists[1:len(artists):2]:
        artist_arr.append(artist_tag.string)
    print("Title: " + track_name)
    print("Album: " + album_name)
    print("Artists: " + artist_arr[0],end='')
    for artist in artist_arr[1:len(artist_arr)]:
        print(', ' + artist, end='')

def generate_url(title):
    modified_title = title.replace(' ', '+')
    return "http://www.gaana.com/search/songs/" + modified_title

url = generate_url("mitwa")
get_info(url)


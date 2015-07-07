from __future__ import print_function

__author__ = 'sachin'
from bs4 import BeautifulSoup
import urllib2
import json

def get_info(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    # print(soup.prettify())

    track_info_json = json.loads(soup.find(class_='searchsonglist').string)
    track_name = track_info_json['title']
    album_name = track_info_json['albumtitle']
    duration = secs_to_hm(track_info_json['duration'])
    artist_arr = []
    artists = soup.find(class_='artist').contents[1].contents
    for artist_tag in artists[1:len(artists):2]:
        artist_arr.append(artist_tag.string)
    print("Title: " + track_name)
    print("Album: " + album_name)
    print("Artists: " + artist_arr[0],end='')
    for artist in artist_arr[1:len(artist_arr)]:
        print(', ' + artist, end='')
    print()
    print("Duration: " + duration)

def generate_url(title):
    modified_title = title.replace(' ', '+')
    return "http://www.gaana.com/search/songs/" + modified_title

def secs_to_hm(seconds):
    hour = int(seconds)/60
    minutes = int(seconds)%60
    return str(hour) + ":" + str(minutes)

url = generate_url("mitwa")
get_info(url)


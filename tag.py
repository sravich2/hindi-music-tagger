from __future__ import print_function

__author__ = 'sachin'
import requests
import re
import json
import HTMLParser

def get_info(url):
    r = requests.get(url)
    matches = re.findall(r'.*?<div class="hide song-json">(.*?)</div>', r.text, re.S)

    for json_info in matches:
        print_data_from_json(json_info)

def generate_url(title):
    modified_title = title.replace(' ', '-')
    return "http://www.saavn.com/s/" + modified_title

def secs_to_hm(seconds):
    hour = int(seconds/60)
    minutes = int(seconds%60)
    return str(hour) + ":" + '{:02d}'.format(minutes)

def print_data_from_json(track_info):
    track_info_json = json.loads(track_info)
    track_name = HTMLParser.HTMLParser().unescape(track_info_json['title'])
    album_name = HTMLParser.HTMLParser().unescape(track_info_json['album'])
    duration = track_info_json['duration']
    year = track_info_json['year']
    artists = track_info_json['singers']
    music_director = track_info_json['music']

    print("Title: " + track_name)
    print("Album: " + album_name)
    print("Artists: " + artists)
    print("Music Director: " + music_director)
    print("Duration: " + secs_to_hm(int(float(duration))))
    print("Year: " + year + "\n\n")

url = generate_url('mitwa')
get_info(url)

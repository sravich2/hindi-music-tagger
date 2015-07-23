from __future__ import print_function

__author__ = 'sachin'
import requests
import re
import json
#
def get_info(url):
    r = requests.get(url)
    matchObj = re.match(r'.*?<div class="hide song-json">(.*?)</div>', r.text, re.S)
    track_info_json = json.loads(matchObj.group(1))

    track_name = track_info_json['title']
    album_name = track_info_json['album']
    duration = track_info_json['duration']
    year = track_info_json['year']
    artists = track_info_json['singers']
    music_director = track_info_json['music']

    print("Title: " + track_name)
    print("Album: " + album_name)
    print("Artists: " + artists)
    print("Music Director: " + music_director)
    print("Duration: " + secs_to_hm(int(float(duration))))
    print("Year: " + year)

def generate_url(title):
    modified_title = title.replace(' ', '-')
    return "http://www.saavn.com/s/" + modified_title

def secs_to_hm(seconds):
    hour = int(seconds/60)
    minutes = int(seconds%60)
    return str(hour) + ":" + '{:02d}'.format(minutes)

url = generate_url('enna solla pogirai kandukondain')
get_info(url)
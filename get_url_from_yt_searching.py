import re
import requests

from checker import db


SEARCHING_URL = 'https://www.youtube.com/results?search_query='
search_keys = ['rick roll meme', 'rickroll', 'rickroll song', 'never gonna give you up meme']
url_list = [ SEARCHING_URL+key.replace(' ', '+') for key in search_keys ]

def get_urls_from_youtube_searching():
    results = []
    for url in url_list:
        page = requests.get(url)
        pattern = '\"/watch\?v=[^"]*\"'
        results += re.findall(pattern, page.text)
    return list(set(results))

def make_dict_from_list(_urls):
    url_dict = {str(i): url.replace('"', '') for i, url in enumerate(_urls)}
    return url_dict

def add_data_to_firestore(_data):
    db.collection('rickroll').document('urls').set(_data)

urls = get_urls_from_youtube_searching()
data = make_dict_from_list(urls)
add_data_to_firestore(data)

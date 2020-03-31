import re
import requests

def url_find(url):
    url_fetch = requests.get(url)
    url_txt = url_fetch.text
    results = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url_txt)
    url_list = []
    for result in results:
        url_list.append(result)
    if len(url_list) > 0:
        return url_list
    if len(url_list) == 0:
        pass
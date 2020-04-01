#external
import re
import requests

#local
from resources import _imagefind
from resources import _videofind
from resources import _urlfind


class hufflib:

    def __init__(self, url, ext):
        self.url = url
        self.ext = ext

    def url_find(url):
        return _urlfind.url_find(url)       


    def url_imagefind(url, ext):
        return _imagefind.url_imagefind(url=url, ext=ext)

    
    def url_videofind(url, ext):
        return _videofind.url_videofind(url=url, ext=ext)

x = hufflib.url_imagefind('https://www.reddit.com', 'all')

print(x)
        

        

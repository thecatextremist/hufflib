#imagefind example

url_to_fetch = "https://reddit.com/"
url_data = hufflib.url_imagefind(url_to_fetch, 'jpg')
print(url_data)

#videofind example

url_to_fetch = "https://reddit.com/"
url_data = hufflib.url_videofind(url_to_fetch, 'mp4')
print(url_data)

#urlfind example
url_to_fetch = "https://reddit.com/"
url_data = hufflib.url_imagefind(url_to_fetch)
print(url_data)
# Hufflib

Hufflib (html url finder library) is a python library built for extracting urls out of html pages. 
with Hufflib You can extract general urls or specific urls with special extensions such as image urls or video urls.
Hufflib then retrieves the urls and appends them to a list for you! <br> 

You can additionally specify which format the image/video should be in, or you can use 'all' to display all urls. <br>

Currently supported image formats: png, jpg, svg, tiff, bmp, ico. <br>
Currently supported video formats: mp4, webm, ogg, avi, mov, flv. <br>

## Notice: Hufflib is not yet uploaded to pypi! For now, when hufflib is in it's testing stages, just copy the files to your project directory! 

## Examples

```python
import hufflib

#gets urls on page with any image behind them
url_data = hufflib.url_imagefind("https://reddit.com", 'all')
print(url_data)
>>> ['reddit.com/image.png', 'reddit.com/image.ico', 'reddit.com/image.jpg']

#gets urls on page with jpeg images behind them 
url_data = hufflib.url_imagefind("https://reddit.com", 'jpg')
print(url_data)
>>> ['reddit.com/image.jpg'] 

#gets urls on page with only mp4 videos behind them
url_data = hufflib.url_videofind("https://reddit.com", 'mp4')
print(url_data)
>>> ['reddit.com/video.mp4'] 
```

## Contributing
Pull requests are welcome!

## License
[MIT](https://choosealicense.com/licenses/mit/)

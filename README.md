# Hufflib

Hufflib (html url finder library) is a lightweight python library built for extracting urls out of html pages. 
With Hufflib You can extract general urls or specific urls with special extensions such as: image urls, video urls or audio urls.<br>
TL;DR Hufflib retrieves urls on a web page and appends them to a list for you! <br>P.S: Hufflib is very helpful in the process of web scraping<br> 

You can additionally specify which format the image/video/audio should be in, or you can use the 'all' option to display all of urls within the page. <br>

Will find all images of the formats: png, jpg, svg, tiff, bmp, ico. <br>
Will find all videoes of formats: mp4, webm, ogg, avi, mov, flv. <br>
Will find all audio of formats: mp3, wav. <br>

## Notice:<br> 
Hufflib is not yet uploaded to pypi, for I am choosing to mature Hufflib more before uploading it to pypi. So For now, when hufflib is in it's testing stages just copy the files to your project directory and it will work! 

## Examples:

```python
import hufflib
```
```python
#gets urls on page with any image behind them
images = hufflib.url_imagefind("https://reddit.com", 'all')
print(images)

>>> ['reddit.com/image.png', 'reddit.com/image.ico', 'reddit.com/image.jpg']
```
```python
#gets urls on page with jpeg images behind them 

images = hufflib.url_imagefind("https://reddit.com", 'jpg')
print(images)

>>> ['reddit.com/image.jpg', 'reddit.com/anotherimage.jpg] 
```
```python
#gets urls on page with only mp4 videos behind them

videos = hufflib.url_videofind("https://reddit.com", 'mp4')
print(videos)

>>> ['reddit.com/video.mp4', 'reddit.com/anothervideo.mp4] 
```
## Methods:
|Function|Parameters|
|---------------|---------|
|urlfind()      | url     |   
|url_imagefind()| url, ext|
|url_videofind()| url, ext|
|url_audiofind()| url, ext|

## Contributing:
Pull requests are welcome!

## License:
[MIT](https://choosealicense.com/licenses/mit/)

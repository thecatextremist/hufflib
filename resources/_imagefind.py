import re
import requests

def url_imagefind(url, ext):

        url_fetch = requests.get(url)
        url_txt = url_fetch.text
        results = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url_txt)

         #Liss of images found within page
        image_png = []
        image_jpg = []
        image_svg = []
        image_tiff= []
        image_bmp = []
        image_ico = []
        image_all = []

        #finds png's on the page
        for png in results:
            if 'png' in png:
                image_png.append(png)
            else:
                 pass

        #finds jpeg's on the page
        for jpg in results:
            if 'jpg' in jpg:
                image_jpg.append(jpg)
            else:
                 pass
    
        #finds svg's on the page
        for svg in results:
            if 'svg' in svg:
                image_svg.append(svg)
            else:
                pass

        #finds tiff's on the page
        for tiff in results:
            if 'tiff' in tiff:
                image_tiff.append(tiff)
            else:
                pass

        #finds bmp's on the page
        for bmp in results:
            if 'bmp' in bmp:
                image_bmp.append(bmp)
            else:
                pass

        for ico in results:
            if 'ico' in ico:
                image_ico.append(ico)
            else:
                pass
    
        if ext.lower() == 'png':
            if len(image_png) > 0:
                return image_png
            else:
                pass
    
        if ext.lower() == 'jpg':
            if len(image_jpg) > 0:
                return image_jpg
            else:
                pass
    
        if ext.lower() == 'svg':
            if len(image_svg) > 0:
                return image_svg
            else:
                pass
    
        if ext.lower() == 'tiff':
            if len(image_tiff) > 0:
                return image_tiff
            else:
                pass
    
        if ext.lower() == 'bmp':
            if len(image_bmp) > 0:
                return image_bmp
            else:
                pass
    
        if ext.lower() == 'ico':
            if len(image_ico) > 0:
                return image_ico
            else:
                pass


        if ext.lower() == 'all':
            if len(image_all) > 0:
                return image_all
            else:
                pass
        if ext.lower() == 'all':
            return image_png + image_jpg + image_svg + image_tiff + image_bmp + image_ico
import re
import requests

def url_videofind(url, ext):
        
        url_fetch = requests.get(url)
        url_txt = url_fetch.text
        results = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url_txt)
        
         #Liss of images found within page
        video_mp4 = []
        video_webm = []
        image_ogg = []
        image_avi = []
        image_mov = []
        image_flv = []
        image_all = []

        #finds png's on the page
        for mp4 in results:
            if 'mp4' in png:
                video_mp4.append(mp4)
            else:
                 pass

        #finds jpeg's on the page
        for webm in results:
            if 'webm' in webm:
                video_webm.append(webm)
            else:
                 pass
    
        #finds svg's on the page
        for ogg in results:
            if 'ogg' in ogg:
                video_ogg.append(ogg)
            else:
                pass

        #finds tiff's on the page
        for avi in results:
            if 'avi' in avi:
                video_avi.append(avi)
            else:
                pass

        #finds bmp's on the page
        for mov in results:
            if 'mov' in mov:
                video_mov.append(mov)
            else:
                pass

        for flv in results:
            if 'flv' in flv:
                video_flv.append(flv)
            else:
                pass
    
        if ext.lower() == 'mp4':
            if len(video_mp4) > 0:
                return video_mp4
            else:
                pass
    
        if ext.lower() == 'webm':
            if len(video_webm) > 0:
                return video_webm
            else:
                pass
    
        if ext.lower() == 'ogg':
            if len(video_ogg) > 0:
                return video_ogg
            else:
                pass
    
        if ext.lower() == 'avi':
            if len(video_avi) > 0:
                return video_avi
            else:
                pass
    
        if ext.lower() == 'mov':
            if len(video_mov) > 0:
                return video_mov
            else:
                pass
    
        if ext.lower() == 'flv':
            if len(video_flv) > 0:
                return video_flv
            else:
                pass


        if ext.lower() == 'all':
            if len(video_all) > 0:
                return video_all
            else:
                pass
        
        if ext.lower() == 'all':
            return video_mp4 + video_webm + video_ogg + video_avi + video_mov + video_flv
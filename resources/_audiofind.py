import re
import requests

def url_audiofind(url, ext):

        url_fetch = requests.get(url)
        url_txt = url_fetch.text
        results = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url_txt)

         #Liss of audio found within page
        audio_mp3 = []
        audio_wav = []
        audio_all = []

        #finds mp3's on the page
        for mp3 in results:
            if 'mp3' in mp3:
                audio_mp3.append(mp3)
            else:
                 pass

        #finds wav's on the page
        for wav in results:
            if 'wav' in wav:
                audio_wav.append(wav)
            else:
                 pass
    
        if ext.lower() == 'mp3':
            if len(audio_mp3) > 0:
                return audio_mp3
            else:
                pass
    
        if ext.lower() == 'wav':
            if len(audio_wav) > 0:
                return audio_wav
            else:
                pass

        if ext.lower() == 'all':
            if len(audio_all) > 0:
                return audio_all
            else:
                pass
        if ext.lower() == 'all':
            return audio_mp3 + audio_wav 
        
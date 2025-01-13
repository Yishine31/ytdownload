from pytube import Playlist
from pytube import YouTube
import re
# 解除 youtube 年齡限制
from pytube.innertube import _default_clients 
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def get_list(url):
    playlist = Playlist(url)
    list = playlist.video_urls
    return list


def get_title(title):
    regex= re.compile(r'[a-zA-Z0-9\u4E00-\u9FFF\uff0c]') # 所有中文字 :\u4E00-\u9FFF  中文逗點 :\uff0c
    arr = re.findall(regex,title)[:-7]
    title = ''.join(arr)
    title = title.split('，')[0]
    return title

def download_audio_keep(url,start,total):
    global finish
    no = total-start+1
    list = get_list(url)
    for url in list[start-1:total]:
        yt = YouTube(url)
        title = yt.title
        title = get_title(title)
        yt.streams.filter().get_audio_only().download(pathdir,filename="{}_{}-({}).mp3".format(title,no,start))
        print(f'{title} -done')
        start+=1
        no-=1
        finish = start
    print('All done!')


def do_keepDownload(start):
    try:
        download_audio_keep(url,start,total)
    except Exception as e:
        print(e)
        print(f'\n{finish} error')
        start=finish
        do_keepDownload(start)

'''正則式使用方法與實例-steam
https://steam.oxxostudio.tw/category/python/example/remove-blank.html
https://steam.oxxostudio.tw/category/python/library/re.html
'''

pathdir = 'D:\python_text\Soundbook\ghost_talk'

url = 'https://www.youtube.com/playlist?list=PLmLHnIXE4fPHo8yzknWEWf1XQGXLpewME'
total = 17
start = 1
finish = 0

# print(folderlist)
do_keepDownload(start)




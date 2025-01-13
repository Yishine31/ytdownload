from pytube import Playlist
from pytube import YouTube
import os
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
# import time

# 解除 youtube 年齡限制
from pytube.innertube import _default_clients 
_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


def download_lsit(url):
    playlist = Playlist(url)
    list = playlist.video_urls
    for url in list:
        yt=YouTube(url)
        title=yt.title
        yt.streams.filter().get_highest_resolution().download(pathdir,filename=f'{title}.mp4')
        print(f'{title} 下載完成')
    print('done!')

def download_lowest_lsit(url):
    playlist = Playlist(url)
    list = playlist.video_urls
    for url in list:
        yt=YouTube(url)
        title=yt.title
        yt.streams.filter().get_lowest_resolution().download(pathdir,filename=f'{title}_low.mp4')
        print(f'{title} 下載完成')
    print('done!')

def download_single(url):
    yt=YouTube(url)
    title=yt.title
    yt.streams.filter().get_highest_resolution().download(pathdir,filename=f'{title}.mp4')
    print(f'{title} 下載完成')
    print('done!')

def download_lowest_single(url):
    yt=YouTube(url)
    title=yt.title
    print(f'{title} 開始下載')
    yt.streams.filter().get_lowest_resolution().download(pathdir,filename=f'{title}.mp4')
    print(f'{title} 下載完成')
    print('done!')


# 將夜 1121來源
# url = 'https://www.youtube.com/watch?v=TGTDcgLDmf4&list=PLxak_2LR4viXCNtLhHk3scJaT7r53IHmy'

# 自建播放清單
url = 'https://www.youtube.com/watch?v=QPfuc0cnRU0&t=655s'
# 建立資夾
pathdir = 'D:\\python_text\\video_mp4'
if not os.path.isdir(pathdir):
    os.mkdir(pathdir)

# download_single(url)
# download_lsit(url)
# download_lowest_lsit(url)
download_lowest_single(url)

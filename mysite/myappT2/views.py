from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
import youtube_dl
import re

# Create your views here.
import pymysql


def t1_view(request,page):
    print("ok...got it!")
    str = "okkkk %s"%page
    return HttpResponse(str)


def login(request):
    return render(request,'common_cxml.html')



class MyLogger(object):
    def debug(self, msg):
        print('debug:'+msg)

    def warning(self, msg):
        print('warning:'+msg)

    def error(self, msg):
        print('error:'+msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def show(request):
    return render(request, 'show.html')


def Find(string):
    # findall() 查找匹配正则表达式的字符串
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url

def get_url(URL):
    url = Find(URL)
    if len(url) == 0:
        raise Exception("urlError")
    # 获取第一个链接
    return url[0]

def miaomiao(request):
    url_str = str(request.GET.get('url', ''))
    dict = {"code":200 , "msg":"ok" , "data":""}
    try:
        # 尝试处理url
        url = get_url(url_str)
        print('url = %s'%url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            dict['data'] = ydl.extract_info(url, download=False)
            #ydl.download([url])
    except BaseException as err:
        # 接收到异常，返回状态码：500  msgß：错误信息 dict ：空
        dict["code"] = 500
        dict["msg"] = err
        return HttpResponse(str(dict))
    else :
        #
        return HttpResponse(str(dict))
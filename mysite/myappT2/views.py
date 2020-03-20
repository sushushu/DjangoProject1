from __future__ import unicode_literals
from django.shortcuts import render,HttpResponse
import youtube_dl
import re
import json
import requests
# Create your views here.
# import pymysql


def t1_view(request,page):
    print("ok...got it!")
    str = "okkkk %s"%page
    return HttpResponse(str)



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
        # url = "https://tv.sohu.com/v/MjAyMDAzMDUvbjYwMDgyMTgxOS5zaHRtbA==.html"
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("dddd%s"%url)
            #ydl.download([url])
            print("ttt%s"%url)

            dict['data'] = ydl.extract_info(url, download=False)

    except BaseException as err:
        # 接收到异常，返回状态码：500  msg：错误信息 dict ：空
        dict["code"] = 500
        dict["msg"] = str(err)
        return HttpResponse(json.dumps(dict))


    else :
        # ok 状态码 200
        return HttpResponse(json.dumps(dict))






HEADERS = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'charset':'utf-8',
    'upgrade-insecure-requests': '1',
    'user-agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
}

TIMEOUT = 10

RETRY = 5

RESULTS_VARIATION_RETRY = 5000

def get_real_address(url):
    if url.find('v.douyin.com') < 0:
        return url
    res = requests.get(url, headers=HEADERS, allow_redirects=False)
    if res.status_code == 302:
        long_url = res.headers['Location']
        HEADERS['Referer'] = long_url
        return long_url
    return None

def get_html(url,headers):
    response = requests.get(url,headers=headers)
    print(response.text)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        return response.text
    return "None"


#正则表达式提取信息
def re_get_ids(url):

    url_wn = re.search("/(\d)+/",url)
    ids = re.sub("/","",str(url_wn.group()))
    return ids

#正则表达式提取信息
def re_get_dytk(text):
    dytk = re.search('dytk: \"([^\"]*)\"', text)
    dytk = re.sub('[dytk: ,\"]','',str(dytk.group()))
    return dytk


def douyin(request):
    url_str = str(request.GET.get('url', ''))
    dict = {"code": 200, "msg": "ok", "data": ""}
    try:
        # 尝试处理url
        url = get_url(url_str)
        print(url)
        long_url = get_real_address(url)
        html_text = get_html(long_url,HEADERS)
        ids = re_get_ids(long_url)
        dytk = re_get_dytk(html_text)
        url_2 = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+ids+"&dytk="+dytk
        dict["data"] = get_html(url_2,HEADERS)
        print(url_2)
        #print(type(dict['data']))


    except BaseException as err:
        # 接收到异常，返回状态码：500  msg：错误信息 dict ：空
        dict["code"] = 500
        dict["msg"] = str(err)
        return HttpResponse(json.dumps(dict),
                content_type="application/json,charset=utf-8")


    else :
        # ok 状态码 200
        return HttpResponse(json.dumps(dict),
                content_type="application/json,charset=utf-8")
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

def f_mm(request):
    return render(request, 'f_mm.html')

def f_dy(request):
    return render(request, 'f_dy.html')

def f_mooc(request):
    return render(request, 'f_mooc.html')


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


def get_long_address(url):
    if url.find('v.douyin.com') < 0:
        return None
    res = requests.get(url, headers=HEADERS, allow_redirects=False)
    if res.status_code == 302:
        long_url = res.headers['Location']
        HEADERS['Referer'] = long_url
        return long_url
    return None

def get_real_address(url):

    res = requests.get(url, headers=HEADERS, allow_redirects=False)
    if res.status_code == 302:
        now_url = res.headers['Location']
        HEADERS['Referer'] = now_url
        return now_url
    return None

def get_html(url,headers = None):

    if headers is None:
        response = requests.get(url,headers = {'content-type': 'charset=utf8'})
    else:
        response = requests.get(url,headers=headers)
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

def re_get_title(text):
    result = re.search('(<div class="user-title">)(.*?)(</div>)', text).group()
    name = re.sub('(<div class="user-title">|</div>)', '', result)
    return name


def douyin(request):
    url_str = str(request.GET.get('url', ''))
    dict = {"code": 200, "msg": "ok", "data": ""}
    try:
        # 尝试处理url
        url = get_url(url_str)
        print(url)
        long_url = get_long_address(url)
        html_text = get_html(long_url,HEADERS)
        ids = re_get_ids(long_url)
        dytk = re_get_dytk(html_text)
        url_2 = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+ids+"&dytk="+dytk

        dict["data"] = json.loads(get_html(url_2))
        play_addrs = dict['data']['item_list'][0]['video']['play_addr']['url_list']
        dict['data']['real_url'] = get_real_address(play_addrs[0])
        dict['data']['title'] = re_get_title(html_text)

        #dict["data"] = url_2

    except BaseException as err:
        # 接收到异常，返回状态码：500  msg：错误信息 dict ：空
        dict["code"] = 500
        dict["msg"] = str(err)
        return HttpResponse(json.dumps(dict),
                content_type="application/json")


    else :
        # ok 状态码 200
        return HttpResponse(json.dumps(dict),
                content_type="application/json")


def mooc(request):
    str_edu_unique_id = str(request.GET.get('edu_unique_id', ''))
    str_mob_token = str(request.GET.get('mob_token', ''))


    return HttpResponse(json.dumps(dict))
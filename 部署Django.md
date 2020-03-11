* conda no found

  * sudo vim  /etc/profile
  * /etc/profile末尾添加：export PATH=/root/anaconda3/bin:$PATH
  * 重启linux

  

+ 指定目录安装虚拟环境	
  + conda create --prefix=/home/mysite_env  python=3.6

+ 启动虚拟环境
  + source activate /home/mysite_env



+ 启动django项目 

  + python manage.py migrate

  + python manage.py runserver  0.0.0.0:80

    + 要注意端口被占用的问题
    + sudo netstat -tulpn | grep :80
    + kill - 9 端口号



+ http://106.14.148.160/show
  + Django初始化admin账号和密码:
     ```	python3 manage.py createsuperuser```



+ 后台运行
  + nohup python  manage.py runserver 0.0.0.0:80 > main.out 2>&1 &



1、v1接口

###### 请求方法：get

###### 请求路径：/api/v1

###### 请求参数：url

###### 返回结果：



+ code : 状态码

  + 200 ok
  + 500 error

+ msg ：返回信息

  + ok
  + 其他

+ data ： 数据

  + title ：文件名
  + description ： 简介
  + url ：链接
  + Referer ： 来源
  + ext ：ext

  

```
{'code': 200, 'msg': 'ok', 'data': {'id': '93525244', 'duration': 430.93, 'formats': [{'url': 'http://cn-gdfs2-cc-bcache-19.bilivideo.com/upgcxcode/01/60/159676001/159676001-1-80.flv?e=ig8euxZM2rNcNbRVhWNBhwdlhWd1hbUVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEVEuxTEto8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&deadline=1583949831&gen=playurl&nbs=1&oi=1779340448&os=bcache&platform=pc&trid=5785dd6aecd3474a9d3731f9933ffa22&uipk=5&upsig=df74bf06317ff9823f5804ce03d578f5&uparams=e,deadline,gen,nbs,oi,os,platform,trid,uipk&mid=0&origin_cdn=ks3', 'preference': -3, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.93 Safari/537.36', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5', 'Referer': 'https://www.bilibili.com/video/av93525244?spm_id_from=333.851.b_7265706f7274466972737431.9'}, 'ext': 'flv', 'format_id': '0', 'format': '0 - unknown', 'protocol': 'http'}, {'url': 'http://cn-sh-cc-bcache-03.bilivideo.com/upgcxcode/01/60/159676001/159676001-1-80.flv?e=ig8euxZM2rNcNbRVhWNBhwdlhWd1hbUVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEVEuxTEto8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&deadline=1583949831&gen=playurl&nbs=1&oi=1779340448&os=bcache&platform=pc&trid=5785dd6aecd3474a9d3731f9933ffa22&uipk=5&upsig=df74bf06317ff9823f5804ce03d578f5&uparams=e,deadline,gen,nbs,oi,os,platform,trid,uipk&mid=0&origin_cdn=ks3', 'preference': -3, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.93 Safari/537.36', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5', 'Referer': 'https://www.bilibili.com/video/av93525244?spm_id_from=333.851.b_7265706f7274466972737431.9'}, 'ext': 'flv', 'format_id': '1', 'format': '1 - unknown', 'protocol': 'http'}, {'url': 'http://cn-cq-gd-bcache-24.acgvideo.com/upgcxcode/01/60/159676001/159676001-1-80.flv?e=ig8euxZM2rNcNbRVhWNBhwdlhWd1hbUVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEVEuxTEto8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&deadline=1583949831&gen=playurl&nbs=1&oi=1779340448&os=bcache&platform=pc&trid=5785dd6aecd3474a9d3731f9933ffa22&uipk=5&upsig=df74bf06317ff9823f5804ce03d578f5&uparams=e,deadline,gen,nbs,oi,os,platform,trid,uipk&mid=0&origin_cdn=ks3', 'filesize': 174822610, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.93 Safari/537.36', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5', 'Referer': 'https://www.bilibili.com/video/av93525244?spm_id_from=333.851.b_7265706f7274466972737431.9'}, 'ext': 'flv', 'format_id': '2', 'format': '2 - unknown', 'protocol': 'http'}], 'title': '【闻香识】一对枪就卡，老是白给怎么办？低延迟模式真的有用吗？该怎么减少画面延迟？', 'description': '希望能够对大家有帮助！快50万啦，求关注！~~唯一指定直播间【www.wenxiangshi.live】 （虎牙290429）通知群660982473，其他聊天群见公告；~ᕕ( ᐛ )ᕗ觉得好看的话欢迎投币点赞收藏支持！！！！！( ͡° ͜ʖ ͡°)微博@_闻香识', 'timestamp': 1583316899, 'thumbnail': 'http://i0.hdslb.com/bfs/archive/2e4d2f5a6611ccce61a4689b75fc3814c8ee035d.jpg', 'uploader': '闻香识', 'uploader_id': '193584', 'extractor': 'BiliBili', 'webpage_url': 'https://www.bilibili.com/video/av93525244?spm_id_from=333.851.b_7265706f7274466972737431.9', 'webpage_url_basename': 'av93525244', 'extractor_key': 'BiliBili', 'playlist': None, 'playlist_index': None, 'thumbnails': [{'url': 'http://i0.hdslb.com/bfs/archive/2e4d2f5a6611ccce61a4689b75fc3814c8ee035d.jpg', 'id': '0'}], 'display_id': '93525244', 'upload_date': '20200304', 'requested_subtitles': None, 'url': 'http://cn-cq-gd-bcache-24.acgvideo.com/upgcxcode/01/60/159676001/159676001-1-80.flv?e=ig8euxZM2rNcNbRVhWNBhwdlhWd1hbUVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEVEuxTEto8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&deadline=1583949831&gen=playurl&nbs=1&oi=1779340448&os=bcache&platform=pc&trid=5785dd6aecd3474a9d3731f9933ffa22&uipk=5&upsig=df74bf06317ff9823f5804ce03d578f5&uparams=e,deadline,gen,nbs,oi,os,platform,trid,uipk&mid=0&origin_cdn=ks3', 'filesize': 174822610, 'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.93 Safari/537.36', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-us,en;q=0.5', 'Referer': 'https://www.bilibili.com/video/av93525244?spm_id_from=333.851.b_7265706f7274466972737431.9'}, 'ext': 'flv', 'format_id': '2', 'format': '2 - unknown', 'protocol': 'http'}}
```
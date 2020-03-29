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
     
     sususu814
     
     meinqisha
  
+ 后台运行

  + nohup python  manage.py runserver 0.0.0.0:80 > mysite_log.txt 2>&1 &



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

+ data ： 抖音数据

  

```json
{"code": 200, "msg": "ok", "data": "{\"status_code\":0,\"item_list\":[{\"image_infos\":null,\"position\":null,\"cha_list\":null,\"desc\":\"\u201c\u603b\u6709\u4e00\u9635\u98ce\u5439\u8fc7\u6211\u518d\u5439\u8fc7\u4f60  \u603b\u6709\u4e00\u4e2a\u77ac\u95f4\u6211\u4eec\u4e4b\u95f4\u7684\u8ddd\u79bb\u662f\u96f6\u201d\u2014\u2014Day115\ud83c\udf51#\u5d14\u771f\u7406 #\u5d14\u96ea\u8389 #IU\",\"video\":{\"has_watermark\":true,\"bit_rate\":null,\"height\":720,\"width\":752,\"origin_cover\":{\"uri\":\"large/tos-cn-p-0015/5c05c4169bb0444e99e09b584ad8e0ed_1580883249\",\"url_list\":[\"http://p3-dy.byteimg.com/large/tos-cn-p-0015/5c05c4169bb0444e99e09b584ad8e0ed_1580883249.jpeg?from=2563711402_large\",\"http://p9-dy.byteimg.com/large/tos-cn-p-0015/5c05c4169bb0444e99e09b584ad8e0ed_1580883249.jpeg?from=2563711402_large\",\"http://p29-dy.byteimg.com/large/tos-cn-p-0015/5c05c4169bb0444e99e09b584ad8e0ed_1580883249.jpeg?from=2563711402_large\"]},\"download_addr\":{\"uri\":\"v0200fc40000bot5qa1pskdp2um3in5g\",\"url_list\":[\"https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fc40000bot5qa1pskdp2um3in5g&line=0&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme&is_support_h265=0&source=PackSourceEnum_PUBLISH\",\"https://api.amemv.com/aweme/v1/play/?video_id=v0200fc40000bot5qa1pskdp2um3in5g&line=1&ratio=540p&watermark=1&media_type=4&vr_type=0&improve_bitrate=0&logo_name=aweme&is_support_h265=0&source=PackSourceEnum_PUBLISH\"]},\"play_addr_lowbr\":{\"uri\":\"v0200fc40000bot5qa1pskdp2um3in5g\",\"url_list\":[\"https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fc40000bot5qa1pskdp2um3in5g&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH\",\"https://api.amemv.com/aweme/v1/play/?video_id=v0200fc40000bot5qa1pskdp2um3in5g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH\"]},\"duration\":24265,\"vid\":\"v0200fc40000bot5qa1pskdp2um3in5g\",\"play_addr\":{\"uri\":\"v0200fc40000bot5qa1pskdp2um3in5g\",\"url_list\":[\"https://aweme.snssdk.com/aweme/v1/play/?video_id=v0200fc40000bot5qa1pskdp2um3in5g&line=0&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH\",\"https://api.amemv.com/aweme/v1/play/?video_id=v0200fc40000bot5qa1pskdp2um3in5g&line=1&ratio=540p&media_type=4&vr_type=0&improve_bitrate=0&is_play_url=1&is_support_h265=0&source=PackSourceEnum_PUBLISH\"]},\"cover\":{\"uri\":\"tos-cn-p-0015/b6b66ab43c944a4b9e1bd20b703593a9_1580883249\",\"url_list\":[\"https://p9-dy.byteimg.com/img/tos-cn-p-0015/b6b66ab43c944a4b9e1bd20b703593a9_1580883249~c5_300x400.jpeg?from=2563711402_large\",\"https://p26-dy.byteimg.com/img/tos-cn-p-0015/b6b66ab43c944a4b9e1bd20b703593a9_1580883249~c5_300x400.jpeg?from=2563711402_large\",\"https://p3-dy.byteimg.com/img/tos-cn-p-0015/b6b66ab43c944a4b9e1bd20b703593a9_1580883249~c5_300x400.jpeg?from=2563711402_large\"]},\"dynamic_cover\":{\"uri\":\"tos-cn-p-0015/cb109f1b9b4c4a3b9f1ef6e3b68cf3de_1580883249\",\"url_list\":[\"https://p9-dy.byteimg.com/obj/tos-cn-p-0015/cb109f1b9b4c4a3b9f1ef6e3b68cf3de_1580883249?from=2563711402_large\",\"https://p1-dy.byteimg.com/obj/tos-cn-p-0015/cb109f1b9b4c4a3b9f1ef6e3b68cf3de_1580883249?from=2563711402_large\",\"https://p3-dy.byteimg.com/obj/tos-cn-p-0015/cb109f1b9b4c4a3b9f1ef6e3b68cf3de_1580883249?from=2563711402_large\"]},\"ratio\":\"540p\"},\"text_extra\":null,\"uniqid_position\":null,\"comment_list\":null,\"aweme_id\":\"6789841806126370052\",\"video_labels\":null,\"duration\":24265,\"label_top_text\":null,\"promotions\":null,\"long_video\":null,\"statistics\":{\"aweme_id\":\"6789841806126370052\",\"comment_count\":137,\"digg_count\":4589},\"video_text\":null,\"geofencing\":null}],\"extra\":{\"now\":1584809810000,\"logid\":\"202003220056500100140460130479C88E\"}}\n"}
```


T2: 接口改成抖音去水印

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

+ Git 的基本使用

1、douyin接口

抖音去水印

###### 请求方法：get

###### 请求路径：/api/v1/douyin

###### 请求参数：url

###### 返回结果：



+ code : 状态码

  + 200 ok
  + 500 error

+ msg ：返回信息

  + ok
  + 其他

+ data ： 抖音数据

  




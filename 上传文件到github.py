# -*- coding:utf-8 -*-

import requests
import json
import base64

url = 'https://api.github.com/repos/'
repo = 'username/Bugs/contents/'
file = '3.txt'
path = url+repo+file
print(path)

userInfo = bytes('hankeboom@163.com:hanqian1993','utf-8')
userInfo_base64 = base64.b64encode(userInfo)
user = 'Basic '+userInfo_base64.decode()
print(user)

header = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
          'Accept' : 'application/json',
          'Accept' : 'application/vnd.github.v3.raw+json',
          'Authorization' : user}

message = 'from my script'
contentInfo = bytes('测试我的脚本', "utf-8")
contentInfo_base64 = base64.b64encode(contentInfo)
content = contentInfo_base64.decode()
bodyRaw={
    'message' : message,
    'content' : content
}


response = requests.put(path,json=bodyRaw,headers=header)
print(response.text)
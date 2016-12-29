# -*- coding:utf-8 -*-
import requests
import re
'''
用到的库：
requests
re(正则)
流程：
手动登录查看需要的参数，观察一次登录发送的请求
               *****
                ***
                 *
发现除了一个token是动态的，其他的都是输入或是固定的。参数如下：
'login':'。。。',
'password':'。。。',
'authenticity_token':token,
'commit':'Sign in',
'utf8': "✓"}
               *****
                ***
                 *
用正则在登录页面爬取登录用的token,并赋值到参数里
               *****
                ***
                 *
接着用会话对象去发送带有参数的数据到url
               *****
                ***
                 *
                完成
'''
s = requests.Session()#获取会话对象，用于登录时的cookie和session
header = {'Host': 'github.com',
          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Language': 'en-US,en;q=0.5',
          'Accept-Encoding': 'gzip, deflate, br',
          'Referer': 'https://github.com',
          'Connection': 'keep-alive'}

indexUrl = 'https://github.com/'#首页地址
loginUrl = 'https://github.com/login'#登录页面
sessionUrl = 'https://github.com/session'#登录页面把表单提交到这个url，然后重定向到首页，把数据提交到这个Url之后可以获取到cookie,用于登录

##>>> payload = {'key1': 'value1', 'key2': 'value2'}
##>>> r = requests.get("http://httpbin.org/get", params=payload)

tokenRule = '<input name="authenticity_token" type="hidden" value="(.*?)"'#登录参数里面有一个token参数，是加载到页面中并且是动态的，需要爬出来
loginHtml = s.get(loginUrl,headers=header)#得到登录页面
tokenPattern = re.compile(tokenRule,re.S)
arraryTolen = re.findall(tokenPattern,loginHtml.text)#得到动态的token,这里返回的事数组，取第一个

#print(loginHtml.text)
token = arraryTolen[0]
print("the token is: ",token)

loginParams = {'login':'hankeboom@163.com',
               'password':'hanqian1993',
               'authenticity_token':token,
               'commit':'Sign in',
               'utf8': "✓"}#配置登录参数
sessionHtml = s.post(sessionUrl,data=loginParams)#得到登录后的页面，其实被定位到了首页
'''
输出是否登录成功，如果不成功返回状态码和原因，以及详细的错误页面
'''
print("the session rsult is: ",sessionHtml.status_code)
print("the reason is: ",sessionHtml.reason)
print("the detail is: ",sessionHtml.text)

indexhtml = s.get('https://github.com/HanlaoTwo/StacknotOverFlow',headers=header)#可以继续用这个会话对象去访问需要登录的页面
print(indexhtml.text)
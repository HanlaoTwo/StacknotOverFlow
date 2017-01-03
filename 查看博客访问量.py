# -*- coding:utf-8 -*-

import requests
import re
'''
实现功能：
查看自己活着别人CSDN中每篇博客的访问量
语言：
Python3.5
用到的库：
requests
re
步骤：
1.找到数据源：找到一个现实所有博客的页面，在一篇博客的右上方可以点击目录查看所有博客的名字和浏览次数。
2.筛选标题：审查元素找到标题对应的位置，观察标题前后的代码，找到规律编写正则表达试。
3.筛选浏览量：同上
4.取数据：爬取页面，用正则表单是匹配标题和浏览量。
5.输出：根据标题对应的访问量输出爬取的内容
结果：
如图
代码：
源码地址：
'''

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br'
}
#步骤1
html = requests.get('http://blog.csdn.net/boomhankers?viewmode=list',headers = header)
print('结果：',html.status_code)
print('原因：',html.reason)
#步骤2、3
rule1 = 'title="阅读次数">阅读<\/a>\((.*?)\)<\/span>'
rule2 = '<span class="link_title"><a href=".*?">(.*?)</a></span>'
patten1 = re.compile(rule1,re.S)
patten2 = re.compile(rule2,re.S)
#步骤4
tileArray = re.findall(patten2,html.text)
timeArray = re.findall(patten1,html.text)
#步骤5
i = 0
for tile in tileArray:
    print(tile+": "+timeArray[i])
    i = i+1

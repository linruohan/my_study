#coding=utf-8
from urllib import request
import urllib
import lxml
import lxml.html as HTML
import lxml.etree as etree
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# url = r'http://www.lagou.com/zhaopin/Python/?labelWords=label'
url = r'http://www.baidu.com/'
headers = {

    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                  'Referer': r'http://www.baidu.com/',
   'Connection': 'keep-alive'
}
req = request.Request(url, headers=headers)
page = request.urlopen(req).read()
page= page.decode('utf-8')
hdoc = HTML.fromstring(page)
htree = etree.ElementTree(hdoc)

# 依次打印出hdoc每个元素的文本内容和xpath路径
for t in hdoc.iter():
    if t.text:
        print (htree.getpath(t))
        print (t.text)

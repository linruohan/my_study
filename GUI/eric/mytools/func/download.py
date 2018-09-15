#coding=utf-8
# 通过python采集时 ，经常需要从html 中获取图片或文件的URL并下载到本地，
# 这里列举最常用的三种模块下载的方法：urllib模块、urllib2模块、requests模块。具体代码如下：
import curl
import io
import pycurl
import urllib
import urllib2
from gevent import monkey
from gevent.pool import Pool
import requests
import sys,os
from os.path import basename
from urllib.parse import urlsplit
monkey.patch_all()
def urllib_down(url):
    url = 'http://www.test.com/wp-content/uploads/2012/06/wxDbViewer.zip'
    print( "downloading with urllib")
    urllib.urlretrieve(url, "code.zip")
def urllib2_down(url):
    print ("downloading with urllib2")
    f = urllib2.urlopen(url)
    data = f.read()
    with open("code2.zip", "wb") as code:
        code.write(data)
# 看起来使用urllib最为简单，一句语句即可。当然你可以把urllib2缩写成：
def urllib2_down2(url):
    f = urllib2.urlopen(url)
    with open("code2.zip", "wb") as code:
       code.write(f.read())
def requests_down(url):
    print ("downloading with requests")
    r = requests.get(url)
    with open("code3.zip", "wb") as code:
        code.write(r.content)
# 上面的方法中，还可以设置timeout参数，避免采集一直阻塞。。
'''      
  pycurl方法下载
'''
def pycurl_down(url):
    ##### init the env ###########
    c = pycurl.Curl()
    c.setopt(pycurl.COOKIEFILE, "cookie_file_name")#把cookie保存在该文件中
    c.setopt(pycurl.COOKIEJAR, "cookie_file_name")
    c.setopt(pycurl.FOLLOWLOCATION, 1) #允许跟踪来源
    c.setopt(pycurl.MAXREDIRS, 5)
    #设置代理 如果有需要请去掉注释，并设置合适的参数
    #c.setopt(pycurl.PROXY, 'http://11.11.11.11:8080')
    #c.setopt(pycurl.PROXYUSERPWD, 'aaa:aaa')
    ########### get the data && save to file ###########
    head = ['Accept:*/*','User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0']
    buf = io.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, buf.write)
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.HTTPHEADER,  head)
    curl.perform()
    the_page =buf.getvalue()
    buf.close()
    f = open("./%s" % ("img_filename",), 'wb')
    f.write(the_page)
    f.close()
'''Python实现批量下载文件'''
class More_down:
    def __init__(self):
        pass
    @staticmethod
    def download(url):
        chrome = 'Mozilla/5.0 (X11; Linux i86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
        headers = {'User-Agent': chrome}
        filename = url.split('/')[-1].strip()
        r = requests.get(url.strip(), headers=headers, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    print(filename, "is ok")
    def removeLine(self,key, filename):
        os.system('sed -i /%s/d %s' % (key, filename))



def url2name(url):
    return basename(urlsplit(url)[2])
def download1(url, localFileName=None):
    localName = url2name(url)
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    if r.info().has_key('Content-Disposition'):
        # If the response has Content-Disposition, we take file name from it
        localName = r.info()['Content-Disposition'].split('filename=')[1]
        if localName[0] == '"' or localName[0] == "'":
            localName = localName[1:-1]
    elif r.url != url:
        # if we were redirected, the real file name we take from the final URL
        localName = url2name(r.url)
        if localFileName:
            # we can force to save the file as specified name
            localName = localFileName
            f = open(localName, 'wb')
            f.write(r.read())
            f.close()
    download1(r'你要下载的python文件的url地址')
if __name__ == "__main__":
    m=More_down()
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        f = open(filename, "r")
        p = Pool(4)
        for line in f.readlines():
            if line:
                p.spawn(m.download, line.strip())
        key = line.split('/')[-1].strip()
        m.removeLine(key, filename)
        f.close()
        p.join()
    else:
        print('Usage: python %s urls.txt' % sys.argv[0])


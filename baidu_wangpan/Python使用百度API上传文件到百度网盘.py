# coding:UTF-8
import urllib
import urllib2
__author__ = 'Administrator'
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

register_openers()

def upload(fileName):
    """
    通过百度开发者 API 上传文件到百度云
    """
    datagen, headers = multipart_encode({"file": open("E:\\PHPTest\\Test1\\%s"%fileName, "rb")})
    baseurl = "https://pcs.baidu.com/rest/2.0/pcs/file?"
    args = {
        "method": "upload",
        "access_token": "0.a2834e35964a7b0704242wef160507c1.2592000.1386326697.1060338330-1668780",
        "path": "/apps/ResourceSharing/%s"%fileName
    }
    encodeargs = urllib.urlencode(args)
    url = baseurl + encodeargs

    print(url)

    request = urllib2.Request(url, datagen, headers)
    result = urllib2.urlopen(request).read()
    print(result)


upload("host.txt")
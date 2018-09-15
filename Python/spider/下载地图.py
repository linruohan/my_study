#coding=utf-8
from os import makedirs
import shutil,os
from urllib import request

def down():
    x="397"
    y="147"
    z="11"
    udt="20180711"
    scale="1"
    ak="E4805d16520de693a3fe707cdc962045"
    customid="dark"
    html="http://api1.map.bdimg.com/customimage/tile?&x=%s&y=%s&z=%s&udt=%s&scale=%s&ak=%s&customid=%s"%(x,y,z,udt,scale,ak,customid)
    path1='F:\\%s\\%s\\%s.jpg'%(z,x,y)
    if not os.path.exists(path1):  # 判断文件夹是否存在
        # shutil.rmtree(path)  # 删除文件夹
        makedirs(os.path.dirname(path1))
        print(os.path.dirname(path1) + ' 创建成功')
    request.urlretrieve(html, 'F:\\%s\\%s\\%s.jpg'%(z,x,y))
    print('%s下载完毕'%path1)
if __name__ == '__main__':
    down()


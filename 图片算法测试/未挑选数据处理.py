# coding=utf-8
import os
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
import pytesseract, os

class parse1:
    def __init__(self,path):
        self.path=path
    def all_path(self):
        result = []
        for maindir, subdir, file_name_list in os.walk(self.path):
            if 'pic' in str(maindir):
                print(maindir)
                print("tiao  .......")
                continue
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)
                result.append(apath)
        # print(result)
        print('共有%s个文件,进行预处理。' % len(result))
        return result


def parse2(path):
    text = pytesseract.image_to_string(Image.open(path), lang='eng+chi_sim+equ')
    return text

path=r"F:\working-xiangxun\aaa——项目\图片算法测试\图片二次分析图片资源\图片\图片 - 副本\1"
p=parse1(path)
# print(p.all_path()[:10])
list =p.all_path() # 列出文件夹下所有的目录与文件
plates,paths=[],[]
for i in list:
    fullpath = os.path.join(path, i)
    # print(fullpath)
    name=os.path.basename(i).replace(u'PLATE', u'PIC')
    s = "http://193.169.100.238:8099/ftp/pic/others/" + name

    if "PLATE" in str(os.path.basename(i)).split('_'):
        # plate=parse2(fullpath)
        # print(plate)
        plates.append(s)

with open('未挑选.txt', 'w', encoding="gbk") as f:
    for i in range(len(plates)):
        # s = '{"610100000000011001", "01", "1", "%s", "2", "01", "A", "K33", "%s", },' % (plates[i], paths[i])
        s = '{"610100000000011001", "01", "1", "甘D80132", "2", "01", "A", "K33", "%s", },' % (plates[i])
        # print(s)
        f.write(s + '\n')
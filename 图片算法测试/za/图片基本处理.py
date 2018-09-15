# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
import pytesseract, os


def parse(path):
    text = pytesseract.image_to_string(Image.open(path), lang='eng+chi_sim+equ')
    return text
path = r"F:\working-xiangxun\aaa——项目\图片算法测试\图片二次分析图片资源\图片\图片\1"

list = os.listdir(path)[:10] # 列出文件夹下所有的目录与文件
for i in list:
    fullpath = os.path.join(path, i)
    print(fullpath)
    if "PLATE" in str(i).split('_'):
        # print(fullpath)
        # plate=parse(fullpath)
        oldname=""
        newname=""
        # os.rename(oldname, newname)

# if os.path.isfile(path): pass
# if
# print(path)

if __name__ == '__main__':
    pass
    # image=all_path(r'C:\Users\mao\Desktop\20180301135148\G30连霍高速西临段K1011临潼方向')
    #
    # print(text)
    # for i in image:
    #     text=pytesseract.image_to_string(Image.open(i),lang='chi_sim')
    #     print(text)

# coding=utf-8
import os
class parse1:
    def __init__(self,path):
        self.path=path
    def all_path(self):
        result = []
        for maindir, subdir, file_name_list in os.walk(self.path):
            if 'pic2' in str(maindir):
                for filename in file_name_list:
                    if "jpg" not in filename:continue
                    apath = os.path.join(maindir, filename)
                    result.append(apath)
        # print(result)
        print('共有%s个文件,进行预处理。' % len(result))
        return result



path=r"D:\ftp\pic2"
p=parse1(path)
# print(p.all_path()[:10])
list =p.all_path() # 列出文件夹下所有的目录与文件
plates,paths,chepais=[],[],[]
for i in list:
    fullpath = os.path.join(path, i)
    # print("fullpath:",fullpath)
    plate="陕AT9971"
    s = '/'+i.split("\\",maxsplit=2)[2].replace('\\','/')
    # print(s)
    plates.append(plate)
    paths.append(s)
with open('第三轮.txt', 'w', encoding="gbk") as f:
    for i in range(len(plates)):
        s = '{"610100000000021001", "01", "1", "%s", "2", "01", "A", "K33", "%s", },' % (plates[i], paths[i])
        # s = '{"610100000000011001", "01", "1", "陕AT9971", "2", "01", "A", "K33", "%s", },' % (paths[i])
        print(s)
        f.write(s + '\n')
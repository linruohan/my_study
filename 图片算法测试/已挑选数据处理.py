import os
class parse:
    def __init__(self,path):
        self.path=path
    def all_path(self):
        result = []
        for maindir, subdir, file_name_list in os.walk(self.path):
            if 'other' in str(maindir) or "other2" in str(maindir):
                print(maindir)
                print("tiao  .......")
                continue
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)
                result.append(apath)
        # print(result)
        print('共有%s个文件,进行预处理。' % len(result))
        return result




if __name__ == '__main__':

    path=r"D:\ftp\pic"
    p=parse(path)
    # print(p.all_path())
    plates,paths=[],[]
    for i in p.all_path():
        # print(os.path.basename(i))
        s="http://193.169.100.238:8099/"+i.split("\\",maxsplit=1)[1].replace(u'\\',u'/')
        # print(s)
        plates.append(os.path.basename(i).split('.')[0])
        paths.append(s)
    # print(plates)
    # print(paths)
    with open('挑选.txt', 'w', encoding="gbk") as f:
        for i in range(len(plates)):
            s = '{"610100000000011001", "01", "1", "%s", "2", "01", "A", "K33", "%s", },' % (plates[i],paths[i])
            print(s)
            f.write(s + '\n')
# -*- coding: cp936 -*-
import os
class Filenames:

    def all_path(self, path):
        result = []
        for maindir, subdir, file_name_list in os.walk(path):
            for filename in file_name_list:
                apath = os.path.join(maindir, filename)
                result.append(apath)
        # print(result)
        print('����%s���ļ�,����Ԥ����' % len(result))
        return result

    def names(self, paths, pattern, type):
        names = []
        for i in paths:
            n = 1
            if i.split('.')[-1] != pattern:
                name = i.split(type)[0]
                if name in names:
                    name += str(n)
                singlename = name.split('\\')[-1]
                names.append(singlename)
        print('�ܹ��õ�%s���ļ���'%len(names))
        return names

    def rename(self, result, pattern, type):
        names = []
        for i in result:
            n = 1
            if not i.split('.')[-1] == pattern:
                name = i.split(type)[0]
                if name in names:
                    name += str(n)
                names.append(name)
                print(name)
                os.rename(i, name + type)
            n += 1


if __name__ == '__main__':
    # ���˵��ļ���ʽ
    pattern = 'onetoc2'
    # �����ļ���ʽ
    type = '.one'
    path ='F:\\onenote�ʼǱ�\\20180321�ʼǱ�\\jintao �ıʼǱ�'
    s = Filenames()
    paths=s.all_path(path)
    names=s.names(paths, pattern, type)
    print(names)
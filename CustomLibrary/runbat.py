#-*- coding:utf-8 -*-
'''
created by bugmaster 2015-01-29
'''
__version__ = '0.1'
from robot.api import logger
import os

class Runbat(object):
    def run_all_bat(self,path):
        u'''接收一个目录的路径，并执行目录下的所有 bat 文件.例
        | run all bat | filepath |
        '''
        for root,dirs,files in os.walk(path):
            for f in files:
                if os.path.splitext(f)[1] == '.bat':
                    os.chdir(root)
                    #print root,f
                    os.system(f)

    def __execute_sql(self, path):
        logger.debug ("Executing : %s" % path)

        print (path)
    def decode(self,customerstr):
        return customerstr.decode('utf-8')
if __name__ == "__main__":
    path = u'D:\\test_boject'
    run = Runbat()
    run.run_all_bat(path)
1#coding=utf-8

'''主程序'''
from mvc.controller.quoteterminalController import QuoteterminalController

def mains():
    while True:
        controller=QuoteterminalController()
        controller.run()







if __name__ == '__main__':
    mains()

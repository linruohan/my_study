#coding=utf-8
import threading 
import socket
 
 
#socket
udpSocket = None
#计数器
num = 1
 
#1.创建接受，发送方法
def inMessage():
    global num
    while True:
        #等待接收消息
        data = udpSocket.recvfrom(1024)
        #4. 将接收到的数据再发送给对方
        udpSocket.sendto(data[0], data[1])
        #打印获得的消息
        print("\r>> 消息%d => 来自:%s => %s"%(num,data[1],data[0].decode('gb2312')))
        print('\r>>',end='')
        #消息数量+1
        num+=1
 
def outMessage():
    while True:
        #发送地址
        sendAddr = ('32.32.32.33',8888)
        #获得输入数据
        senddata = input('\r>>')
        #发送消息
        udpSocket.sendto(senddata.encode('gb2312'),sendAddr)
 
 
#2.使用多线程执行接收发送
def main():
    global udpSocket
   
   #创建socket
    udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定端口
    udpSocket.bind(('',8888))
 
    #创建线程
    t1 = threading.Thread(target=inMessage)
    t2 = threading.Thread(target=outMessage)
 
    #启动线程
    t1.start()
    t2.start()
 
    #主线程堵塞
    t1.join()
    t2.join()
 
#3.主方法运行
if __name__ == "__main__":
    main()
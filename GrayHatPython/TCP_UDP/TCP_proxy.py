import sys
from  socket import *
from threading import Thread

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):

    '''开启服务端'''
    server=socket(AF_INET,SOCK_STREAM)
    try:
        server.bind((local_host,local_port))
    except:
        print("[!!] failed to listen on %s:%d"%(local_host,local_port))
        print("[!!] Check for other listening sockets or correct permissions.")
        sys.exit(0)
    print("[*] Listening in %s:%d"%(local_host,local_port))

    server.listen(5)
    while True:
        client_socket,addr=server.accept()
        print("[==>]Received incoming connection from %s:%d"%(addr[0],addr[1]))
        proxy_thread=Thread(target=proxy_handle,args=(client_socket,remote_host,remote_port,receive_first))
        proxy_thread.start()

def proxy_handle(client_socket,remote_host,remote_port,receive_first):
    '''代理客户端'''
    remote_socket=socket(AF_INET,SOCK_STREAM)
    remote_socket.connect((remote_host,remote_port))
    # if neccessary， recv data from remotePC
    if receive_first:
        remote_buffer=receive_from(remote_socket)
        hexdump(remote_buffer)
        #send to response handle
        remote_buffer=response_handler(remote_buffer)
        #if has data ,send it to local_socket
        if len(remote_buffer):
            print("[<==] Sending %d bytes  to localhost."%len(remote_buffer) )
            client_socket.send(remote_buffer.encode("utf-8"))
    #now reading data from localclient,send it to remotehost and localhost
    while True:
        # reading data from local client
        '''client==>proxy==>server'''
        local_buffer=receive_from(client_socket)
        if len(local_buffer):
            print("[==>] Received %d bytes from localhost."%len(local_buffer) )
            hexdump(local_buffer)
            #send to local request
            local_buffer=request_handler(local_buffer)
            #send data to remote PC
            remote_socket.send(local_buffer.encode("utf-8"))
            print("[==>] Send to remote.")
        #receive response data
        '''client<==proxy<==server'''
        remote_buffer=receive_from(remote_socket)
        if len(remote_buffer):
            print("[<==] Received %d bytes from remote."%len(remote_buffer))
            hexdump(remote_buffer)
            # send response to handle
            remote_buffer=response_handler(remote_buffer)
            # send response to local socket
            client_socket.send(remote_buffer.encode("utf-8"))
            print("[<==] Sent to localhost.")
        # if two sides has neither no data,close connecting
        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print("[*] No more data. Closing connections.")
            break
def main():

    if len(sys.argv[1:])!=5:
        print("Useage:./proxy.py [localhost][localport][remotehost][remoteport][receivedfirst]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)
    local_host=sys.argv[1]
    local_port=int(sys.argv[2])

    remote_host=sys.argv[3]
    remote_port=int(sys.argv[4])

    #tell proxy before sending:connect and recv data to remotePC
    receive_first=sys.argv[5]
    if "True" in receive_first:
        receive_first=True
    else:receive_first=False
    #setting the listening socket
    server_loop(local_host,local_port,remote_host,remote_port,receive_first)

def hexdump(src,length=16):
    '''16进制导出函数
    仅仅输出数据包的十六进制和可打印的ASCII码字符
    用来了解未知的协议，还可以找到使用明文协议的认证信息
    '''
    result=[]
    digits=4 if isinstance(src,str) else 2
    for i in range(0,len(src),length):
        s=src[i:i+length]
        # %0*X: %X 16进制转换 0靠右对齐 * 占长度=digits
        hexa=" ".join(["%0*X" %(digits,ord(x)) for x in s])# %X:格式化无符号十六进制数（大写）
        text=''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append("%04X   %-*s  %s"%(i,length*(digits+1),hexa,text))
        print('\n'.join(result))
def receive_from(connection):
    buffer=""
    lent = 1
    #我们设置了两秒的超时，这取决于目标的情况，可能需要调整
    connection.settimeout(2)
    try:
        #持续从缓存中读取数据直到没有数据或者超时
        while True:
            data=connection.recv(4096)
            if not data: break
            buffer+=data.decode("utf-8")

    except:pass
    return buffer
#对目标时远程主机的请求进行修改
def request_handler(buffer):
    #执行包修改
    return  buffer
#对目标是本地主机的响应进行修改
def response_handler(buffer):
    # 执行包修改
    return buffer


if __name__ == '__main__':
    main()
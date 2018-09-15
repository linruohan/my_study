import configparser
# --read():读取配置文件
# --sections():读取配置文件中所有的section(可以理解为组名:group1,group2……)
# --options(section):读取该section下所有的option(可以理解成读取该组下的所有key)
# --items(section):读取该section下的所有值,并以键值对形式输出(例如:(‘name’:‘name1’))
# --get(section, option):读取指定section下面的option的值(可以理解成,读取具体某个group下面指定key的值)
# --add_section(section):添加一个section,参数为section的名称
# --set(section, option, value):在section下面添加一条数据(key=value),需要调用write()将内容写入文件
config=configparser.ConfigParser()
ini=config.read('001.ini')
print(config.sections())
print(config.items('group2'))
print(config.get('group2','name'))
print(config.set('group2','name','123'))
with open('001.ini','w') as f:
    config.write(f)
# print(config.add_section('new_section'))
if __name__ == '__main__':
    pass
    # print("所有节点==>", config.sections())
    # print("包含实例范围默认值的词典==>", config.defaults())
    # for item in config["DEFAULT"]:
    #     print("循环节点topsecret.server.com下所有option==>", item)
    # print("bitbucket.org节点下所有option的key，包括默认option==>", config.options("bitbucket.org"))
    # print("输出元组，包括option的key和value", config.items('bitbucket.org'))
    # print("bitbucket.org下user的值==>", config["bitbucket.org"]["user"])  # 方式一
    # topsecret = config['bitbucket.org']
    # print("bitbucket.org下user的值==>", topsecret["user"])  # 方式二
    # print("判断bitbucket.org节点是否存在==>", 'bitbucket.org' in config)
    # print("获取bitbucket.org下user的值==>", config.get("bitbucket.org", "user"))
    # print("获取option值为数字的:host port=", config.getint("topsecret.server.com", "host port"))
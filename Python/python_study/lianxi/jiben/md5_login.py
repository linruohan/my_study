# -*- coding: utf-8 -*-
import  hashlib
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
#
# def calc_md5(password):
#     pass
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
#
# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    sha=hashlib.md5()
    sha.update(password.encode('utf-8'))
    # print(sha)
    secret=sha.hexdigest()
    print(secret)
    return True if db[user]==secret else False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
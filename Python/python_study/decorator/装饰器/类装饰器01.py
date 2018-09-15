def bar(s):
    print(123)

def int(c):
    c.bar=bar
    return c

@int
class m(object):
    print("class inner")


s=m()
s.bar()

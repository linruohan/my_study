from random import sample
def s():
    # str = ''.join(sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789',7))0123456789
    str = '黑'+''.join(sample('ABCDEFGHIJKLMNOPQ',1))+''.join(sample('ABCDEFGHIJKLMNOPQ0123456789',5))
    return str
if __name__ == '__main__':
    print(s())

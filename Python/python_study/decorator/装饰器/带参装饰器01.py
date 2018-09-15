import time

def fun01(s=True):
    if s:
        def fun01(func):
            def counter(*args,**kwargs):
                start=time.clock()
                func(*args,**kwargs)
                end=time.clock()
                print("userd time :%d" %(end-start,))
            return counter
    else:
        def fun01(func):
            return func
    return fun01

@fun01(True)
def add(x,y):
    time.sleep(3)
    print("add result:%d" %(x+y,))

@fun01(False)
def mul(x,y=1):
    print("mul result:%d" %(x*y,))


add(1,5)
mul(10)

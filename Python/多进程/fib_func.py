from functools import wraps

def cache(func):
    caches ={}
    @wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args]= func(*args)
        return caches[args]
    return wrap
@cache
def fib(n):
    if n <2:return 1
    return fib(n-1)+ fib(n-2)

print (fib(10))#call fib so easy!
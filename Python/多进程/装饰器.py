from functools import wraps
def f(func):
    caches = {}
    @wraps(func)
    def wrap(*args):
        if args not in caches:
            caches[args] = func(*args)
        return caches[args]
    return wrap
@f
def s(m):
    print('1222',m)
    return m**2
print(s(3))
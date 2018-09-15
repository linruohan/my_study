def decorator_a(func):
    def inner(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return inner

@decorator_a
def foo():
    '''''foo doc'''
    return 'foo result'

foo()
print(str(foo.__doc__))
print 'foo.__module__: ' + str(foo.__module__)
print 'foo.__name__: ' + str(foo.__name__)
print 'foo.__doc__: ' + str(foo.__doc__)
# print foo()

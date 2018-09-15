def decorator_a(func):
    print("decorator_a")
    print("func id:"+ str(id(func)))
    return func


def decorator_b(func):
    print("decorator_b")
    print("func id:"+ str(id(func)))
    return func

print("begin declare foo with decorators")
@decorator_a
@decorator_b
def foo():
    print("foo")

print("end declare foo with decorators")

print("first call foo")
foo()
print("second call foo")
foo()
print("function infos")
print("decorator_a id:"+str(id(decorator_a)))
print("decorator_b id:"+str(id(decorator_b)))
print("foo id:"+str(id(foo)))

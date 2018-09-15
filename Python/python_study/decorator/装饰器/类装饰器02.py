class Foo(object):
    """docstring for Foo."""
    def __init__(self, func):
        super(Foo, self).__init__()
        self.__func = func
    def __call__(self):
        print("class decorator")
        self.__func()


@Foo
def bar():
    print("bvbar")

bar()

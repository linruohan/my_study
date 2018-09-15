class Foo(object):
    """docstring for Foo."""
    @classmethod
    def class_method(s):
        print(repr(s))

    def member_method(self):
        print(repr(self))


f=Foo()
f.member_method()
f.class_method()

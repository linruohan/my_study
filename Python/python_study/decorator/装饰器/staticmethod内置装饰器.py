class Foo(object):
    """docstring for Foo."""
    @staticmethod
    def static_method(msg):
        print(msg)

    def member_method(self,msg):
        print(msg)


f=Foo()
f.member_method("sdfsadfa")
f.static_method("static  msg")
Foo.static_method("chang shi hero ling")

class Foo(object):
    """docstring for Foo."""
    def __init__(self, var):
        super(Foo, self).__init__()
        self._var = var

    @property
    def var(self):
        return self._var

    @var.setter
    def var(self, var):
        self._var=var


f=Foo("var 1")
print(f.var)
f.var="var 2"
print(f.var)

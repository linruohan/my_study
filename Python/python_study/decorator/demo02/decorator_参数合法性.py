
import inspect
import re

class ValidateException(Exception): pass


def validParam(*varargs, **keywords):
    '''验证参数的装饰器。'''

    varargs = map(_toStardardCondition, varargs)#（func,list）将其转换成新列表list
    keywords = dict((k, _toStardardCondition(keywords[k]))
                    for k in keywords)#（转换成新字典格式）

    def generator(func):
        #generator发生器
        args, varargname, kwname = inspect.getargspec(func)[:3]
        dctValidator = _getcallargs(args, varargname, kwname,
                                    varargs, keywords)
        #wrapper包装
        def wrapper(*callvarargs, **callkeywords):
            dctCallArgs = _getcallargs(args, varargname, kwname,
                                       callvarargs, callkeywords)

            k, item = None, None
            try:
                for k in dctValidator:
                    if k == varargname:
                        for item in dctCallArgs[k]:
                            assert dctValidator[k](item)
                    elif k == kwname:
                        for item in dctCallArgs[k].values():
                            assert dctValidator[k](item)
                    else:
                        item = dctCallArgs[k]
                        assert dctValidator[k](item)
            except:
                raise ValidateException,\
                       ('%s() parameter validation fails, param: %s, value: %s(%s)'
                       % (func.func_name, k, item, item.__class__.__name__))

            return func(*callvarargs, **callkeywords)

        wrapper = _wrapps(wrapper, func)
        return wrapper

    return generator


def _toStardardCondition(condition):
    '''将各种格式的检查条件转换为检查函数'''
    #isinstance判断是否是实例化
    if inspect.isclass(condition):
        return lambda x: isinstance(x, condition)

    if isinstance(condition, (tuple, list)):
        cls, condition = condition[:2]
        if condition is None:
            return _toStardardCondition(cls)

        if cls in (str, unicode) and condition[0] == condition[-1] == '/':
            return lambda x: (isinstance(x, cls)
                              and re.match(condition[1:-1], x) is not None)

        return lambda x: isinstance(x, cls) and eval(condition)

    return condition


def nullOk(cls, condition=None):
    '''这个函数指定的检查条件可以接受None值'''

    return lambda x: x is None or _toStardardCondition((cls, condition))(x)


def multiType(*conditions):
    '''这个函数指定的检查条件只需要有一个通过'''

    lstValidator = map(_toStardardCondition, conditions)
    def validate(x):
        for v in lstValidator:
            if v(x):
                return True
    return validate


def _getcallargs(args, varargname, kwname, varargs, keywords):
    '''获取调用时的各参数名-值的字典'''

    dctArgs = {}
    varargs = tuple(varargs)
    keywords = dict(keywords)

    argcount = len(args)
    varcount = len(varargs)
    callvarargs = None

    if argcount <= varcount:
        for n, argname in enumerate(args):
            dctArgs[argname] = varargs[n]

        callvarargs = varargs[-(varcount-argcount):]

    else:
        for n, var in enumerate(varargs):
            dctArgs[args[n]] = var

        for argname in args[-(argcount-varcount):]:
            if argname in keywords:
                dctArgs[argname] = keywords.pop(argname)

        callvarargs = ()

    if varargname is not None:
        dctArgs[varargname] = callvarargs

    if kwname is not None:
        dctArgs[kwname] = keywords

    dctArgs.update(keywords)
    return dctArgs


def _wrapps(wrapper, wrapped):
    '''复制元数据'''

    for attr in ('__module__', '__name__', '__doc__'):
        setattr(wrapper, attr, getattr(wrapped, attr))
    for attr in ('__dict__',):
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

    return wrapper


#===============================================================================
# 测试
#===============================================================================


def _unittest(func, *cases):
    for case in cases:
        _functest(func, *case)


def _functest(func, isCkPass, *args, **kws):
    if isCkPass:
        func(*args, **kws)
    else:
        try:
            func(*args, **kws)
            assert False
        except ValidateException:
            pass

def _test1_simple():
    #检查第一个位置的参数是否为int类型：
    @validParam(int)
    def foo1(i): pass
    _unittest(foo1,
              (True, 1),
              (False, 's'),
              (False, None))

    #检查名为x的参数是否为int类型：
    @validParam(x=int)
    def foo2(s, x): pass
    _unittest(foo2,
              (True, 1, 2),
              (False, 's', 's'))

    #验证多个参数：
    @validParam(int, int)
    def foo3(s, x): pass
    _unittest(foo3,
              (True, 1, 2),
              (False, 's', 2))

    #指定参数名验证：
    @validParam(int, s=str)
    def foo4(i, s): pass
    _unittest(foo4,
              (True, 1, 'a'),
              (False, 's', 1))

    #针对*和**参数编写的验证器将验证这些参数包含的每个元素：
    @validParam(varargs=int)
    def foo5(*varargs): pass
    _unittest(foo5,
              (True, 1, 2, 3, 4, 5),
              (False, 'a', 1))

    @validParam(kws=int)
    def foo6(**kws): pass
    _functest(foo6, True, a=1, b=2)
    _functest(foo6, False, a='a', b=2)

    @validParam(kws=int)
    def foo7(s, **kws): pass
    _functest(foo7, True, s='a', a=1, b=2)


def _test2_condition():
    #验证一个10到20之间的整数：
    @validParam(i=(int, '10<x<20'))
    def foo1(x, i): pass
    _unittest(foo1,
              (True, 1, 11),
              (False, 1, 'a'),
              (False, 1, 1))

    #验证一个长度小于20的字符串：
    @validParam(s=(str, 'len(x)<20'))
    def foo2(a, s): pass
    _unittest(foo2,
              (True, 1, 'a'),
              (False, 1, 1),
              (False, 1, 'a'*20))

    #验证一个年龄小于20的学生：
    class Student(object):
        def __init__(self, age): self.age=age

    @validParam(stu=(Student, 'x.age<20'))
    def foo3(stu): pass
    _unittest(foo3,
              (True, Student(18)),
              (False, 1),
              (False, Student(20)))

    #验证一个由数字组成的字符串：
    @validParam(s=(str, r'/^\d*$/'))
    def foo4(s): pass
    _unittest(foo4,
              (True, '1234'),
              (False, 1),
              (False, 'a1234'))


def _test3_nullok():
    @validParam(i=nullOk(int))
    def foo1(i): pass
    _unittest(foo1,
              (True, 1),
              (False, 'a'),
              (True, None))

    @validParam(i=nullOk(int, '10<x<20'))
    def foo2(i): pass
    _unittest(foo2,
              (True, 11),
              (False, 'a'),
              (True, None),
              (False, 1))


def _test4_multitype():
    @validParam(s=multiType(int, str))
    def foo1(s): pass
    _unittest(foo1,
              (True, 1),
              (True, 'a'),
              (False, None),
              (False, 1.1))

    @validParam(s=multiType((int, 'x>20'), nullOk(str, '/^\d+$/')))
    def foo2(s): pass
    _unittest(foo2,
              (False, 1),
              (False, 'a'),
              (True, None),
              (False, 1.1),
              (True, 21),
              (True, '21'))

def _main():
    d = globals()
    from types import FunctionType
    print
    for f in d:
        if f.startswith('_test'):
            f = d[f]
            if isinstance(f, FunctionType):
                f()

if __name__ == '__main__':
    _main()

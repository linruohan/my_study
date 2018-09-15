# -*- coding: utf-8 -*-
# common/decorator.py

def decorator_a(func):
    print 'init decorator_a'
    return func

@decorator_a
def foo():
    print ('function foo')

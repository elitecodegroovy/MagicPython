#!/usr/bin/env python
__author__ = 'JohnLiu'

def testIt(func, *nkwargs, **kwargs):
    try:
        value = func(*nkwargs, **kwargs)
        result = (True, value)
    except Exception, diag:
        result = (False, str(diag))
    return result

def test():
    funcs = (int, long, float)
    values = (1234, 12.34, '1234', '12.34')
    for eachFunc in funcs:
        print '-' * 20
        for eachValue in values:
            retValue = testIt(eachFunc, eachValue)
            if retValue[0]:
                print '%s(%s) =' % (eachFunc.__name__, str(eachValue)), retValue[1]
            else:
                print '%s(%s) = FAILED:' % (eachFunc.__name__,str(eachValue)), retValue[1]
    print '-'*20

if __name__ == '__main__':
    test()
#!/usr/bin/env python
__author__ = 'JohnLiu'

from time import ctime, sleep

def decoFunction(func):
    def wrappedFunc():
        print '[%s], %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@decoFunction
def doSomething():
    pass

for i in range(3):
    sleep(1)
    doSomething()

#Non-keyword Variable Arguments (Tuple)
def tupleFunc(arg1, arg2 = 'Python', *args):
    print 'argument 1:' + arg1, ', argument 2:'+ arg2
    for eachOne in args:
        print 'another argument: ' +eachOne

tupleFunc('Hello ')
tupleFunc("professional ", 'Java', 'python', 'C++')

#Keyword Variable Arguments (Dictionary)
def dictionaryFunc(arg1, arg2='Python', **args):
    print 'argument 1 :' + arg1, ',argument 2: '+ arg2
    for eachOne in args.keys():
        print 'dictionary args: %s: %s' % (eachOne, str(args[eachOne]))
dictionaryFunc('Java')
dictionaryFunc('Java', 'C', scriptLanguage='Python', scriptJVM='Groovy')

def tupleDictFunc(arg1, arg2='Python', *tuple, **dict):
    print 'arg 1: '+ arg1, ', argument 2 :'+ arg2
    for eachTuple in tuple:
        print 'tuple element : '+ eachTuple
    for key in dict.keys():
        print 'dictionary element : %s: %s' % \
              (key, str(dict[key]))

tupleDictFunc('javascript', 'Java', 'Scala',
             'Groovy', machineLang = 'C', machineLangOO='C++')
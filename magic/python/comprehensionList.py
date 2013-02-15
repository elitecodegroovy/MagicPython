#usr/bin/env python                     --start up line (Unix)
"This is a common module"          # module documentation
from random import randint
from functools import partial
import sys                             # module import
import os
__author__ = 'JohnLiu'               # variables declaration

# print the number which is no remainder if it divides 4.
squared = [x ** 2 for x in range(50) if not x % 4]
for i in squared:
    print i,
#module
sys.stdout.write('\nHello, Python!\n')
print sys.platform  #platform info
print sys.version   #sys version info
print dir()         #global variables
print dir(sys)      #specify the sys variables
print dir(os)       #specify the os variables
#swap two variables in python
x, y = 1, 2
print x , y ,'\n swap:'
x, y = y, x
print x, y

def displayNumType(number):
    if isinstance(number, (int, float, long, complex)):
        print number, 'is a number of type:', type(number).__name__
    else:
        print number, ' is not a number at all!!'


displayNumType(9999)
displayNumType(-22.2)
displayNumType(-5.2+1.9j)
displayNumType('xxx')

#mutable type :
aList = ['ammonia', 83, 85, 'lady']
aList[2] = aList[2] + 1
print aList
print 99999 ** 4
#Conversion Factory Functions
print int(4.9999999), float(4), long(4), complex(4)
#ASCII conversion
print ord('A'), ord('a'), chr(65), chr(97)
#Extended Slicing with Stride Indices
_temp = 'i love python!'
print _temp[::-1], _temp[::2] ,('Faye', 'Leanna', 'Daylen')[-100:100]
#More on Slice Indexing
_temp = 'May best wishes follow you everyday!'
#using None as an index has the same effect as a missing index
for i in ([None] + range(-1, -len(_temp), -1)):
    print _temp[:i]

#Hexadecimal Output
print '%x'% 255,'%#X'% 255, '%#x' % 255
#assert statement
assert range(3) == [0, 1, 2]

#def odd(n):
#    print 'the number value is %s' % str(n)
#    return n % 2
#allNumb = []
#for eachIndex in range(9):
#    allNumb.append(randint(0, 999))
#print 'odd number in list :\n',filter(odd, allNumb)
#refactor
print [n for n in [randint(1, 999) for i in range(9)] if n%2]
#print map(lambda x: x**3, range(6))
print [x**3 for x in range(6)]
print map(lambda x, y: (x+y, x-y), [1,3,5], [2,4,6])
print 'the total is:', reduce((lambda x,y: x+y), range(5))

#partial functional programming
baseTwo = partial(int , base = 2)
baseThree = partial(int , base = 3)
print 'string binary sequence 101(base2:%s, base3:%s), ' % \
       (baseTwo('101'), baseThree('101')), int('101', base=2)

j, k = 1, 2
def proc_1():
    j, k = 3, 4
    print 'proc_1, j == %s, k == %s' % (j, k)
    k = 5

def proc_2():
    j = 6
    proc_1()
    print 'proc_2,j == %s, k == %s' % (j, k)

k = 7
proc_1()
print 'j == %s, k == %s' % (j, k)
j = 8
proc_2()
print 'j == %s, k == %s' % (j, k)

#generator
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
             count += 1

count = counter(5)
for eachCount in count:
    print "counter : %s" % eachCount
    if(eachCount == 8):
        print 'jump out of the loop'
        break

print os.path
print  sys.modules.keys()
print 'all global names %s' % globals().keys()
print 'all local names %s'% locals().keys()

class TestStaticMethod:
    #you can use the '@staticmethod' decorator instead of the definition of code block 'foo = staticmethod(foo)'
    def foo():
        print 'calling static method foo()'
    foo = staticmethod(foo)
class TestClassMethod:
    #you can use the '@classmethod' decorator instead of the definition of code block 'foo = staticmethod(foo)'
    def foo(cls):
        print 'foo() is part of class:', cls.__name__
    foo = classmethod(foo)

tsm = TestStaticMethod()
TestStaticMethod.foo()
tsm.foo()
#test class method
tcm = TestClassMethod()
tcm.foo()
TestClassMethod.foo()

class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))

print RoundFloat(1.294), RoundFloat(1.2953), RoundFloat(1.2990), isinstance('4', str), isinstance(4, int)

# execute the os command:   print os.system('dir')



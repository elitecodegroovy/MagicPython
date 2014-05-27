__author__ = 'JohnLiu'

import re
pat = re.compile(r'([A-Za-z]+)-([A-Za-z]+)')

s = 'This is a te- test of back-references in Python. To change the pattern a-b.'
print re.sub(pat, r'\1 \2', s)

line = "Cats are smarter than dogs"

matchObj = re.search( r'(.*) are(\.*)', line, re.M|re.I)

if matchObj:
     print "matchObj.group() : ", matchObj.group(0)

programming = 'PythonProgramming'
for i in range(-1,  - len(programming), -1):
    print i, programming[:i]
#double string
print programming * 2
#-------------------advanced section-------------------
#[tuple]tuple can be modified
aTuple = ('robots', 77, 93, 'try')
print aTuple[1:3] == (77, 93)

# for i in [10, 11, 12]:
#     print i,
#range build-in function
for i in range(3):
    print i,
print '\n'

#enumerate function
for i, ch in enumerate(programming):
    print ch, '(%d)' % i,
#fancies things like what be selective of what to include in a new line
squared = [x ** 2 for x in range(8) if not x % 2]
for i in squared:
    print i,

#document comment "----document comments-----"
# use help function if you are not familiar with some function.
print help(raw_input)

#[open] build-in function,which is identical for the function file(),
#  #read content from the file
pyFile = open('MongoDBDemo', 'r')
print '''
----------------------------MongoDBDemo.py -----------------------------
'''
for line in pyFile:
    print line,
#type function
print type(pyFile), aTuple

pyFile.close()
'''
tips:
    1. Thus it is important to bear in mind that most modules are
       created solely to be imported rather than to execute asscripts.
    2. safer code is written such that everything is ina function
       except for the code that should be executed on an import of a
       module. Again, usually only the main application module has
       the bulk of the executable code at its highest level.
    3. "Is there a wayfor Python to detect at runtime whether this
        module was imported or executed directly?"
           __name__ contains module name if imported
           __name__ contains '__main__' if executed directly
    4. although integers and strings are immutable objects, Python
       sometimes caches them to be more efficient.
    Data Type Storage Model Update Model Access Model
    Numbers Scalar Immutable Direct
    Strings Scalar Immutable Sequence
    Lists Container Mutable Sequence
    Tuples Container Immutable Sequence
    Dictionaries Container Mutable Mapping
'''
x = 12
y = x
print 'reference previously', y
x = 23
print 'changed after reassigning the new value to x', y

#if a pair of variables do indeed refer to the same object:is and is not operators
#id(a) == id(b) is the same to the expression
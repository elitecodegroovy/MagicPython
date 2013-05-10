__author__ = 'JohnLiu'

import copy

print tuple('abc')
print tuple(('abc', 'a basic sequence'))

aTuple = (123, 'abc', 4.56, ['inner', 'tuple'], 7-9j)
print aTuple[2:], '\n', aTuple[:2]

t = (['xyz', 123], 23, -103.4)
t = t + ('free', 'easy')
print t
print cmp(t, (['xyz', 123], 23, -103.4, 'free', 'easy')) == 0

#we described how object assignments are simply object references. This means
# that when you create an object, then assign that object to another variable, Python does not copy the
# object. Instead, it copies only a reference to the object.

#In the example below, we show two ways of copying an object,
# one uses slices and the other a factory function
#------show copy-------
person = ['name', ['savings', 100.00]]
hubby = person[:]
wife = list(person)
print [id(x) for x in person, hubby, wife], person,  hubby, wife
hubby[0] = 'John Liu'
wife[0] = 'Anna Nash'
hubby[1][1] = 10000000.00
wife[1][1] = 100000.00
print person, hubby, wife
# A shallow copy of an object is defined to be a
# newly created object of the same type as the original object whose contents are references to the
# elements in the original object. In other words, the copied object itself is new, but the contents are not.
# Shallow copies of sequence objects are the default type of copy and can be made in any number of
# ways: (1) taking a complete slice [:], (2) using a factory function, e.g., list(), dict(), etc., or (3)
# using the copy() function of the copy module.

#--------deepcopy-------dereference the original address.
d_hubby = copy.deepcopy(person)
#copy() creates shallow copy, and deepcopy() creates a deep copy
d_wife = copy.deepcopy(wife)
d_hubby[1][1] = 9000.00
d_wife[1][1] = 6000.00
print d_hubby, d_wife
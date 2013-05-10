__author__ = 'JohnLiu'

class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#Python protects those members by internally changing the name to
# include the class name. You can access such attributes as object._className__attrName
# the attribute must start with "__" two underscores.
print counter._JustCounter__secretCount

#---------useful functions
# dir([obj]) Display attributes of object or the names of global variables if no
#            parameter given
# help([obj]) Display object's documentation string in a pretty-printed format or
#              enters interactive help if no parameter given
# int(obj) Convert object to an integer
# len(obj) Return length of object
# open(fn, mode) Open file fn with mode ('r' = read, 'w' = write)
# range([[start, ]stop[,step]) Return a list of integers that begin at start up to but not including stop
#       in increments of step; start defaults to 0, and step defaults to 1
# raw_input(str) Wait for text input from the user, optional prompt string can beprovided
# str(obj) Convert object to a string
# type(obj) Return type of object (a type object itself!)

x, y = 1, 2
print x, y
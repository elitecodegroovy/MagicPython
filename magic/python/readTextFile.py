__author__ = 'JohnLiu'
fileName = 'pythonMakeAFile.txt'
try:
    fobj = open(fileName, 'r')
except IOError, e:
    print "***file open error", e
else:
    #print the file content
    for eachLine in fobj:
        print eachLine
    fobj.close()
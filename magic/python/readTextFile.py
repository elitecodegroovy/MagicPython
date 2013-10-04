__author__ = 'JohnLiu'
import os

fileName = 'readTextFile.py'
try:
    lines = open(fileName, 'r')
    data = [line.strip() for line in lines.readlines()]
    for data in data:
        print data
except IOError, e:
    print "***file open error", e
# else:
#     for eachLine in lines:
#         print eachLine
#     lines.close()
for tmpdir in ('/TEMP', r'c:\TEMP'):
    if os.path.isdir(tmpdir):
        break
    else:
        print 'No directory is available!'

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** current temporary directory'
    print cwd
    print '*** creating example directory...'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working directory:'
    print cwd
    print '*** original directory listing:'
    print os.listdir(cwd)

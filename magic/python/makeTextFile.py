__author__ = 'JohnLiu'
#!/usr/bin/env python
'makeTextFile.py -- create tet file'

import os
from pyquery import PyQuery as pyq
# get filename
file_name = 'pythonMakeAFile.txt'
#while True:
#    if os.path.exists(file_name):
#        print "ERROR: '%s' already exists" % file_name
#        break
#    else:
#        break

 # get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit).\n"

# loop until user terminates input
while True:
    entry = raw_input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

 # write lines to file with proper line-ending
fobj = open(file_name, 'w')
fobj.writelines(['%s%s' % (x, '\n') for x in all])
fobj.close()
print 'DONE!'

#need install third-part library lxml
doc=pyq(url=r'http://list.taobao.com/browse/cat-0.htm')
cts=doc('.market-cat')

for i in cts:
    print '====',pyq(i).find('h4').text(),'===='
    for j in pyq(i).find('.sub'):
        print pyq(j).text() ,
    print '\n'
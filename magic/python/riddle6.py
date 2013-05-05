__author__ = 'JohnLiu'

import zipfile,re
idx="90052"
file = zipfile.ZipFile("channel.zip", "r")
history = []
while True:
    history.append(idx)
    data = file.read(idx+".txt")
    print "File",idx+":\t"+ data
    idx="".join(re.findall('(\\d+)',data))
    if len(idx)==0:
        break

print ''.join([file.getinfo(i+ '.txt').comment for i in history])

__author__ = 'JohnLiu'

import re
pat=re.compile(r'([A-Za-z]+)-([A-Za-z]+)')

s = 'This is a te- test of back-references in Python. To change the pattern a-b.'
print re.sub(pat, r'\1 \2', s)

line = "Cats are smarter than dogs"

matchObj = re.search( r'(.*) are(\.*)', line, re.M|re.I)

if matchObj:
     print "matchObj.group() : ", matchObj.group(0)

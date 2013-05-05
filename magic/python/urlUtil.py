__author__ = 'JohnLiu'

import urllib2
import re

req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
response = urllib2.urlopen(req)
the_page = response.read()
number = re.findall('(\d+)', the_page)
while True:
    req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'% number)
    response = urllib2.urlopen(req)
    the_page = response.read()
    print the_page
    match_list =  re.findall('(\d+)', the_page)
    if match_list:
        number = match_list[0]
        print number
    else:
        break

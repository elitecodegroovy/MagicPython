__author__ = 'JohnLiu'

import urllib2
import re

#------------------------------------------------------------
#Add the proxy if you failed to connect the internet directly.
#------------------------------------------------------------
# proxy_support = urllib2.ProxyHandler({"http":"http://127.0.0.1:8087"})
# opener = urllib2.build_opener(proxy_support)
# urllib2.install_opener(opener)

req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
response = urllib2.urlopen(req)
the_page = response.read()
number = re.findall('(\d+)', the_page)
print number
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

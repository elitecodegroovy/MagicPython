__author__ = 'JohnLiu'

import string
#riddle one:
print "2**38 = %d", 2**38

#riddle two
number_unknown = []
known_str= []
answer = ''
unknown= "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for i in unknown:
  number_unknown.append(ord(i) + 2)

for j in number_unknown:
    c = chr(j-2)
    if( c.isalpha() and c!= 'y' and c != 'z'):
        known_str.append(chr(j))
    else:
        if(c == 'y'):
            known_str.append('a')
        elif(c == 'z'):
            known_str.append('b')
        else:
            known_str.append(c)

for s in known_str:
    answer += s
print answer
#step 2
#ask me to translate the challenge 2 URL to the final target URL. Namely, what's the 'map' should be translated to ?
url= "http://www.pythonchallenge.com/pc/def/map"
mapper = string.maketrans(unknown, answer)
#strip the string ended with slash . The final three string sequence is the answer.
#Yeah, as you seen. It is the acronym to a software technology.
print url.translate(mapper)

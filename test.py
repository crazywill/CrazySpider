#!/usr/bin/env python


import os
import sys
import re
args=sys.argv
result=os.popen('ping -c %d www.weibo.com'%(int(args[1])))
doc=result.read()
pattern=re.compile('time=.*? ')
tmp = pattern.finditer(doc)
total=0
for item in tmp:
    time=int(item.group().split('=')[1].rstrip(' '))
    total+=time
print 'averge time is %d'%(total/int(args[1]))

#coding=utf-8

import re

x='My 2 favorite number are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)
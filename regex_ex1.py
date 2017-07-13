#!/usr/bin/env python
import re

with open("show_int_fa4.txt") as f:

     output = f.read()

match = re.search (r"(\d+) packets input, (\d+) bytes", output)

a= match.group(1)
print('Input %s' % a)

print(match.group(1))
       
print(match.group(2))

match = re.search (r"(\d+) packets output, (\d+) bytes", output)
print(match.group(1))
       
print(match.group(2))

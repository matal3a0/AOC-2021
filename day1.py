#!/usr/bin/env python

import sys

data = ([int(i) for i in sys.stdin.readlines()])

p = data[0]
c = 0

for d in data:
    if d > p:
        c += 1
    p = d

print('Increments a:', c)

p = data[0] + data[1] + data[2]
c = 0

for i in range(len(data)-2):
    s = data[i] + data[i+1] + data[i+2]
    if s > p:
        c += 1
    p = s

print('Increments b:', c)
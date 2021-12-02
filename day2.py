#!/usr/bin/env python

import sys

data = sys.stdin.readlines()

# Part 1
horiz, depth = 0, 0
for d, v in [d.split() for d in data]:
    v = int(v)
    if d == 'forward':
        horiz += v
    elif d == 'down':
        depth += v
    elif d == 'up':
        depth -= v

print('Part 1:', horiz * depth)

# Part 2
horiz, depth, aim = 0, 0, 0
for d, v in [d.split() for d in data]:
    v = int(v)
    if d == 'forward':
        horiz += v
        depth += (aim * v)
    elif d == 'down':
        aim += v
    elif d == 'up':
        aim -= v

print('Part 2:', horiz * depth)


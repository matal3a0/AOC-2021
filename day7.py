#!/usr/bin/env python

import sys

data = [int(x) for x in sys.stdin.readline().split(',')]

cheapest_cost = 10000000000000
for x in range(max(data)):
    temp_cost = 0
    for d in data:
        temp_cost += abs(d - x)

    if temp_cost < cheapest_cost:
        cheapest_cost  = temp_cost

print('Part 1:', cheapest_cost)


cheapest_cost = 10000000000000
for x in range(max(data)):
    temp_cost = 0
    for d in data:
        temp_cost += sum(range(abs(d-x)+1))

    if temp_cost < cheapest_cost:
        cheapest_cost  = temp_cost

print('Part 2:', cheapest_cost)
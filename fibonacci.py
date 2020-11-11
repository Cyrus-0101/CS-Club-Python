#!/usr/bin/env python3
# Copyright 2018-2020 GCN http://www.0101solutions.consulting/

# Simple fibonacci series
# The sum of two elements defines the next set

a, b = 0, 1
while b < 10000:
    print(b, end = ' ', flush = True)
    a, b = b, a + b

print() # line ending

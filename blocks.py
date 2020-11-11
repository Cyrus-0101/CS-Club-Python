#!/usr/bin/env python3
# Copyright 2018-2020 GCN http://www.0101solutions.consulting/

def main():
    hello(3, 6)
    


x = 42 
y = 73
# In Python Blocks do not limit the scope of a variable. 
# Functions do but blocks do not.
def hello(a, b):
    a
    b
    c = a + b
    return print(c)

if x < y:
    print('x < y: x is {} and y is {}'.format(y, x))


if __name__ == '__main__': main()

#!/usr/bin/env python3
# Copyright 2018-2020 GCN http://www.0101solutions.consulting/

import platform

def main():
    message()
    
# In Python an expression is any combination of literals, identifiers and operators.
# Generally anything that returns a value is an expression.

def message():
    print('This is python version {}'.format(platform.python_version()))

# This forces the interpreter to read through the entire script before executing any line of code.
# This allows a more procedural style of programming.
if __name__ == '__main__': main()

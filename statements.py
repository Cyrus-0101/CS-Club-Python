#!/usr/bin/env python3
# Copyright 2018-2020 GCN http://www.0101solutions.consulting/

# IMPORTANT! In Python a statement is a line of code.
import platform
# The assignment below is a statement even if its a line of code.
version = platform.python_version()
# Format is a method of the string object itself not the print function.
print('This is python version {}'.format(version))
# The above print function is also a statement, because it returns a value.
print(f'This is python version {version}')
# The above line of code is similar to the previous one. The f is similar to format
# This is how interpolation and string formatting works in Python.
#!/usr/bin/env python3
# Copyright 2018-2020 GCN http://www.0101solutions.consulting/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True

def list_primes():
    for n in range(100):
        if isprime(n):
            # Flush arguement flushes the output buffer.
            # End instead of starting a new line, end the print there and starts again.
            print(n, end=', ', flush=True)
    print()

list_primes()
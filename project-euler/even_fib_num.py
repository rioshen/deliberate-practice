#!/usr/bin/env python

__author__ = 'Rio'

def even_fib(n):
    a, b = 0, 1
    while a < n:
        if not a % 2:
            yield a
        a, b = b, a+b

print sum(even_fib(4000000))

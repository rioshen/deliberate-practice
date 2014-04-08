#!/usr/bin/env python

__author__ = 'Rio'

from itertools import product

def is_palidrome(num):
    return str(num) == str(num)[::-1]

def largest_palidrome_product():

    multiples =  ((a, b) for a, b in product(xrange(100, 999), repeat=2) if is_palidrome(a*b))
    return max(multiples, key=lambda (a, b): a*b)

a, b = largest_palidrome_product()
print a*b

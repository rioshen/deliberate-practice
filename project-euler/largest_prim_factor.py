#!/usr/bin/env python

__author__ = 'Rio'

def largest_factor(n):
    if n == 1: return 1

    count = 2
    while n > 1:
        if n % count == 0:
            n = n / count
        else:
            count += 1

    return count

#Test Case
print largest_factor(600851475143)

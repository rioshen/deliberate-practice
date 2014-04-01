#!/usr/bin/env python

__author__ = "Rio"

''' Project euler, problem 48 - self powers.'''

def selfpower(num):
    '''
    Get the last ten digits of the num series.

    Use built-in function - pow(x, y) to calculate single power.
    '''
    sum = 0
    for i in xrange(1, num):
        sum += pow(i, i)

    return sum % 10000000000

def self_power(num):
    '''
    Refact it in a more pythonic way.
    '''
    return str(sum([value**value for value in xrange(1, num)]))[-10:]

if __name__ == '__main__':
    print selfpower(1000)
    print self_power(1000)


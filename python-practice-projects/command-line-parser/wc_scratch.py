#!/usr/bin/env python

import sys
import os.path

__author__ = 'Rio'

def valid(filename):
    if not os.path.exists(filename):
        sys.stdout.write('No such file or directory')
        return False
    elif not os.path.isfile(filename):
        sys.stdout.write('%s is not a file' % filename)
        return False
    return True

def count(filename):
    ''' Counts lines, words, characters in a single file
    '''
    with open(filename) as f:
        lines, words, chars = 0, 0, 0
        for k, v in enumerate(f):
            words += len(v.split(' '))
            chars += len(v.strip()) + 1
        lines = k + 1
    return (lines, words, chars)

def wc(files):
    if len(files) == 1 and valid(files):
        lines, words, chars = count(files)
        sys.stdout.write('      %d     %d     %d %s' % (lines, words, chars, files))
        return

    lines, words, chars = 0, 0, 0
    for filename in files:
        if not valid(filename):
            pass
        else:
            a, b, c = count(filename)
            lines += a
            words += b
            chars += c
            result =

if __name__ == '__main__':
    n = len(sys.argv[1:])
    if n == 0:
        sys.exit('usage: %s file' % sys.argv[0])
    else:
        wc(sys.argv[1:])

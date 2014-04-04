#!/usr/bin/env python

# cat command from scratch.
# cat's general syntax is
#     cat [options] [filenames] [-] [filenames]
# I don't think OOP is a good way to do something in scratch. Function is enough.

__author__ = "Rio"

import os
import sys

def usage(info):
    '''
    Prompt usage information and terminal the program.
    '''
    sys.exit('usage: python %s [-benstuv] [file ...]' % info)

def dispatcher(files):
    for filename in files:
        read(filename)

def read(filename):
    if not os.path.exists(filename):
        sys.exit('%s: No such file or directory' % filename)

    if not os.path.isfile(filename):
        sys.exit('%s Is not a directory' % filename)
    else:
        with open(filename) as f:
            print f.read(),

if __name__ == '__main__':
    n = len(sys.argv[1:])
    if n == 0:
        usage(sys.argv[0])
    #elif sys.argv[1].startswith('-'):
        #read(sys.argv[1])
    else: # files
        dispatcher(sys.argv[1:])

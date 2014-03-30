#!/usr/bin/env python

import unittest

__author__ = "Rio"
__version__ = "1.0"

def binary_search(l, val):
    ''' Binary search
    '''
    lo, hi = 0, len(l) - 1

    while lo <= hi:
        mid = lo + (hi - lo) / 2
        if l[mid] > val: hi = mid - 1
        elif l[mid] < val: lo = mid + 1
        else: return mid

    return -1

class BinarySearchTest(unittest.TestCase):

    def test_one(self):
        self.assertEqual(-1, binary_search([], 3))
        self.assertEqual(-1, binary_search([1], 3))
        self.assertEqual(0, binary_search([1, 3, 5], 1))
        self.assertEqual(1, binary_search([1, 3, 5], 3))
        self.assertEqual(2, binary_search([1, 3, 5], 5))
        self.assertEqual(0, binary_search([1, 3, 5, 7], 1))
        self.assertEqual(1, binary_search([1, 3, 5, 7], 3))

if __name__ == '__main__':
    unittest.main()

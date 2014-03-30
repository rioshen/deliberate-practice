#!/usr/bin/env python

import unittest
from double_list import *

class DoubleListTest(unittest.TestCase):
    def double_test_one(self):
        print "Start to run test one"
        lst = DoubleList()

        self.assertEqual(None, lst.find("fred"))
        lst.add("fred")
        self.assertEqual("fred", lst.find("fred").value)

        self.assertEqual(None, lst.find("wilma"))
        lst.add("wilma")
        self.assertEqual("wilma", lst.find("wilma").value)

        self.assertEqual("fred", lst.find("fred").value)
        self.assertEqual("wilma", lst.find("wilma").value)

        self.assertEqual(['fred', 'wilma'], lst.values())

    def double_test_two(self):
        lst = DoubleList()
        lst.add("fred")
        lst.add("wilma")
        lst.add("betty")
        lst.add("barney")

        self.assertEqual(["fred", "wilma", "betty", "barney"], lst.values())

if __name__ == '__main__':
    unittest.main()

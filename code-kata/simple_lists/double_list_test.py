#!/usr/bin/env python

import unittest
from double_list import *

class DoubleListTest(unittest.TestCase):
    def test_double_one(self):
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

    def test_double_two(self):
        lst = DoubleList()
        lst.add("fred")
        lst.add("wilma")
        lst.add("betty")
        lst.add("barney")

        self.assertEqual(["fred", "wilma", "betty", "barney"], lst.values())
        lst.delete(lst.find("wilma"))
        self.assertEqual(["fred", "betty", "barney"], lst.values())
        lst.delete(lst.find("barney"))
        self.assertEqual(["fred", "betty"], lst.values())
        lst.delete(lst.find("betty"))
        self.assertEqual(["fred"], lst.values())
        lst.delete(lst.find("fred"))
        self.assertEqual([], lst.values())

    def test_double_three(self):
        '''
        Test double linked list unique feature - traverse in two directions.
        '''
        lst = DoubleList()
        lst.add("fred")
        lst.add("wilma")
        lst.add("betty")
        lst.add("barney")
        self.assertEqual("fred", lst.find("wilma").prev.value)

if __name__ == '__main__':
    unittest.main()

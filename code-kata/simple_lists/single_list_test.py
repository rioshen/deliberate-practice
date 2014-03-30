import unittest
from single_list import SingleList

class ListTest(unittest.TestCase):

    def test_single_one(self):
        lst = SingleList()
        self.assertEqual(None, lst.find("fred"))
        lst.add("fred")
        self.assertEqual("fred", lst.find("fred").value)
        self.assertEqual(None, lst.find("wilma"))

        lst.add("wilma")
        self.assertEqual("wilma", lst.find("wilma").value)
        self.assertEqual(["fred", "wilma"], lst.values())

    def test_single_two(self):
        lst = SingleList()
        lst.add("fred")
        lst.add("wilma")
        lst.add("betty")
        lst.add("barney")
        self.assertEqual(["fred", "wilma", "betty", "barney"], lst.values())

        lst.delete(lst.find("wilma"))
        self.assertEqual(["fred", "betty", "barney"], lst.values())

        lst.delete(lst.find("barney"))
        self.assertEqual(["fred", "betty"], lst.values())

        lst.delete(lst.find("fred"))
        self.assertEqual(["betty"], lst.values())

        lst.delete(lst.find("betty"))
        self.assertEqual([], lst.values())

if __name__ == '__main__':
    unittest.main()

import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_all(self):
        t_list = OrderedList()
        t_list.add(1)
        t_list.add(3)
        t_list.add(5)
        t_list.add(6)
        t_list.add(9)
        t_list.add(2)
        self.assertFalse(t_list.add(1))
        t_list.remove(1)
        self.assertEqual(t_list.index(1), None)
        self.assertEqual(t_list.remove(22), False)
        self.assertTrue(t_list.search(3))
        t_list2 = OrderedList()
        self.assertEqual(t_list2.index(3), None)
        self.assertFalse(t_list2.remove(2))
        with self.assertRaises(IndexError):
            t_list2.pop(3)
        self.assertFalse(t_list2.search(4))
        self.assertEqual(t_list2.python_list(), [])
        self.assertEqual(t_list2.python_list_reversed(), [])
        self.assertEqual(t_list2.size(), 0)
        t_list3 = OrderedList()
        t_list3.add(99)
        t_list3.add(3)
        t_list3.add(43)
        self.assertEqual(t_list3.index(100), None)
        self.assertEqual(t_list3.pop(2), 99)
        self.assertFalse(t_list3.search(4))
        t_list4 = OrderedList()
        t_list4.add(99)
        t_list4.add(3)
        t_list4.add(43)
        self.assertEqual(t_list4.python_list(), [3, 43, 99])
        self.assertEqual(t_list4.python_list_reversed(), [99, 43, 3])
        self.assertEqual(t_list4.size(), 3)
        self.assertEqual(t_list4.index(99), 2)
        self.assertEqual(t_list4.index(3), 0)

    def test_pop(self):
        t_list = OrderedList()
        t_list.add(3)
        t_list.add(5)
        t_list.add(1)
        t_list.add(2)
        t_list.add(10)
        self.assertEqual(t_list.pop(2), 3)
        self.assertEqual(t_list.add(3), True)
        self.assertEqual(t_list.python_list(), [1, 2, 3, 5, 10])
        t_list.pop(3)
        self.assertEqual(t_list.python_list(), [1, 2, 3, 10])

    def test_is_empty(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list2 = OrderedList()
        t_list2.add(3)
        self.assertFalse(t_list2.is_empty())

    def test_add(self):
        t_list = OrderedList()
        t_list.add(4)
        t_list.add(5)
        t_list.add(1)
        self.assertEqual(t_list.pop(0), 1)
        self.assertEqual(t_list.python_list(), [4, 5])
        self.assertEqual(t_list.python_list_reversed(), [5, 4])
        self.assertFalse(t_list.add(4))

    def test_remove(self):
        t1 = OrderedList()
        self.assertFalse(t1.remove(2))
        t2 = OrderedList()
        t2.add(2)
        t2.add(1)
        t2.add(10)
        self.assertTrue(t2.remove(2))

    def test_index(self):
        t1 = OrderedList()
        t1.add(1)
        t1.add(91)
        t1.add(53)
        self.assertEqual(t1.index(91), 2)
        self.assertEqual(t1.index(0), None)

    def test_pop2(self):
        t1 = OrderedList()
        t1.add(3)
        t1.add(5)
        with self.assertRaises(IndexError):
            t1.pop(-1)
        with self.assertRaises(IndexError):
            t1.pop(2)
        self.assertEqual(t1.pop(1), 5)
        self.assertEqual(t1.python_list(), [3])

    def test_search(self):
        t = OrderedList()
        t.add(1)
        t.add(79)
        t.add(999)
        self.assertFalse(t.search(80))
        self.assertTrue(999)

    def test_size(self):
        t = OrderedList()
        self.assertEqual(t.size(), 0)
        t2 = OrderedList()
        t2.add(4)
        t2.add(3)
        self.assertEqual(t2.size(), 2)




if __name__ == '__main__': 
    unittest.main()

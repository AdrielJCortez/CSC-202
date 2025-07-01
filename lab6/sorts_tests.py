import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple1(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_simple2(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_insert(self):
        nums = [10, 20, 30]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 2)
        self.assertEqual(nums, [10, 20 ,30])

    def test_worst_best_avg_selection(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 45)
        self.assertEqual(nums, [1, 2, 3, 4, 5,6, 7, 8, 9, 10])

    def test_worst_insert(self):
        nums = [5, 4, 3, 2, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_best_insert(self):
        nums = [1, 2, 3, 4, 5]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 4)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_avg_insert(self):
        nums = [1, 3, 2, 4, 5]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 5)
        self.assertEqual(nums, [1, 2, 3, 4, 5])




if __name__ == '__main__': 
    unittest.main()

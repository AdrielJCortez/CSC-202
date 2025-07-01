import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self) -> None:
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter2(self) -> None:
        tlist = []
        expected = None
        result = max_list_iter(tlist)
        self.assertEqual(expected, result)

    def test_max_list_iter3(self) -> None:
        tlist = [-1, -2, -3, 0, -9]
        expected = 0
        result = max_list_iter(tlist)
        self.assertEqual(expected, result)

    def test_max_list_iter4(self) -> None:
        tlist = [19, 4, 7, 18, 12]
        expected = 19
        result = max_list_iter(tlist)
        self.assertEqual(expected, result)

    def test_reverse_rec(self) -> None:
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec2(self) -> None:
        self.assertEqual(reverse_rec([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_reverse_rec3(self) -> None:
        self.assertEqual(reverse_rec([]), [])

    def test_reverse_rec4(self) -> None:
        self.assertEqual(reverse_rec([3]), [3])

    def test_reverse_rec5(self) -> None:
        t_list = None
        with self.assertRaises(ValueError):
            reverse_rec(t_list)

    def test_bin_search(self) -> None:
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)

    def test_bin_search2(self) -> None:
        list_val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(bin_search(3, 0, len(list_val) - 1, list_val), 3)

    def test_bin_search3(self) -> None:
        list_val = []
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)

    def test_bin_search4(self) -> None:
        list_val = [0, 1, 2, 3, 4, 5]
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 5)

    def test_bin_search5(self) -> None:
        list_val = [0, 1, 2]
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1)

    def test_bin_search6(self) -> None:
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(1, 0, 3, list_val)

    def test_reverse_list_mutate(self) -> None:
        list_val = [1, 2, 3]
        expected = [3, 2, 1]
        reverse_list_mutate(list_val)
        self.assertEqual(expected, list_val)

    def test_reverse_list_mutate2(self) -> None:
        list_val = []
        expected = []
        reverse_list_mutate(list_val)
        self.assertEqual(expected, list_val)

    def test_reverse_list_mutate3(self) -> None:
        list_val = None
        with self.assertRaises(ValueError):
            reverse_list_mutate(list_val)



if __name__ == "__main__":
        unittest.main()

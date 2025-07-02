import unittest
from heap import *

class TestHeap(unittest.TestCase):
    def test_enqueue(self):
        t = MaxHeap(7)
        t.enqueue(1)
        t.enqueue(4)
        t.enqueue(2)
        t.enqueue(3)
        self.assertEqual(t.dequeue(), 4)
        self.assertEqual(t.peek(), 3)
        self.assertEqual(t.contents(), [3, 1, 2])

    def test_01_enqueue(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertTrue(insert)
        self.assertEqual(test_heap.contents(), [10, 6, 9, 2, 5, 7, 8])
        self.assertEqual(test_heap.get_size(), 7)

    def test_enqueue_false(self):
        test_heap = MaxHeap(1)
        test_heap.enqueue(1)
        self.assertFalse(test_heap.enqueue(4))
        self.assertEqual(test_heap.dequeue(), 1)
        self.assertEqual(test_heap.dequeue(), None)

    def test_peek_none(self):
        test_heap = MaxHeap(34)
        self.assertEqual(test_heap.peek(), None)
        self.assertEqual(test_heap.dequeue(), None)

    def test(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])


    def test_02_dequeue(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 9)
        self.assertEqual(test_heap.get_size(), 5)
        self.assertEqual(test_heap.contents(), [8, 6, 7, 2, 5])

    def test_03_heap_contents(self):
        test_heap = MaxHeap(8)
        test_heap.build_heap([1, 2, 3])
        self.assertEqual(test_heap.contents(), [3, 2, 1])

    def test_04_build_heap(self):
        test_heap = MaxHeap(10)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_05_is_empty(self):
        test_heap = MaxHeap(5)
        self.assertTrue(test_heap.is_empty())

    def test_06_is_full(self):
        test_heap = MaxHeap(2)
        built = test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())

    def test_07_get_heap_cap(self):
        test_heap = MaxHeap(7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        insert = test_heap.enqueue(10)
        self.assertEqual(test_heap.get_capacity(), 7)

    def test_08_get_size(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.get_size(), 6)

    def test_09_perc_down(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_down(1)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_10_perc_up(self):
        test_heap = MaxHeap()
        test_heap.build_heap([2, 9, 8, 6, 5, 7])
        test_heap.perc_up(6)
        self.assertEqual(test_heap.contents(), [9, 6, 8, 2, 5, 7])

    def test_11_heap_sort_ascending(self):
        test_heap = MaxHeap(10)
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])

    def test3(self):
        t = MaxHeap(3)
        t.enqueue(3)
        self.assertEqual(t.dequeue(), 3)
        self.assertEqual(t.contents(),[])
        t.enqueue(2)
        t.enqueue(2)
        self.assertTrue(t.enqueue(1))
        self.assertEqual(t.dequeue(), 2)

    def test_duplicate_keys(self):
        heap = MaxHeap()
        keys = [41, 28, 41]
        for key in keys:
            heap.enqueue(key)
        contents = heap.contents()
        self.assertTrue(contents == [41, 28, 41] or contents == [41, 41, 28])


if __name__ == "__main__":
    unittest.main()

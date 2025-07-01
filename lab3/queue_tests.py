import unittest

# Use the imports below to test either your array-based queue
# or your link-based version
# It does not matter which import is commented in or out for your final submission

#from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''***Trivial*** test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.enqueue(1)
        q.dequeue()
        q.size()

    def test_init(self):
        q = Queue(4)
        self.assertEqual(4, q.capacity)
        self.assertEqual(0, q.num_items)

    def test_is_empty(self):
        q = Queue(5)
        self.assertTrue(q.is_empty())

    def test_is_empty2(self):
        q = Queue(5)
        q.enqueue(4)
        self.assertFalse(q.is_empty())

    def test_is_full(self):
        q = Queue(3)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertTrue(q.is_full())

    def test_is_full2(self):
        q = Queue(5)
        self.assertFalse(q.is_full())

    def test_enqueue(self):
        q = Queue(1)
        q.enqueue(34)
        with self.assertRaises(IndexError):
            q.enqueue(4)

    def test_enqueue2(self):
        q = Queue(4)
        q.enqueue(3)
        q.enqueue(32)
        self.assertEqual(2, q.num_items)

    def test_enqueue3(self):
            # Create a queue with capacity 5
            queue = Queue(5)

            # Enqueue 3 items
            queue.enqueue(1)
            queue.enqueue(2)
            queue.enqueue(3)
            self.assertEqual(queue.num_items, 3)


            queue.enqueue(4)
            self.assertEqual(queue.num_items, 4)


            queue.enqueue(5)
            self.assertEqual(queue.num_items, 5)

    def test_enqueue4(self) -> None:
        q = Queue(3)
        q.enqueue(2)
        q.enqueue(1)
        q.enqueue(4)
        self.assertEqual(q.size(), 3)
        with self.assertRaises(IndexError):
            q.enqueue(3)

    def test_dequeue(self):
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_dequeue2(self):
        q = Queue(3)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(8)
        self.assertEqual(3, q.dequeue())

    def test_dequeue3(self):
        q = Queue(3)
        q.enqueue(3)
        self.assertEqual(3, q.dequeue())

    def test_dequeue4(self):
        q = Queue(3)
        q.enqueue(6)
        q.enqueue(1)
        q.enqueue(9)
        q.dequeue()
        q.dequeue()

        q.enqueue(5)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 9)
        self.assertEqual(q.num_items, 1)
    def test_size(self):
        q = Queue(5)
        q.enqueue(34)
        q.enqueue(47)
        q.enqueue(8)
        q2 = Queue(1)
        self.assertEqual(3, q.size())
        self.assertEqual(0, q2.size())
        self.assertNotEqual(0, q.size())
        self.assertNotEqual(3, q2.size())


if __name__ == '__main__': 
    unittest.main()

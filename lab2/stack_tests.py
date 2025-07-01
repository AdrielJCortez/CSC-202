import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# It does not matter which import is commented in or out for your submission
from stack_array import Stack
# from stack_linked import Stack


class TestLab2(unittest.TestCase):
    def test_simple(self) -> None:
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    def test_2(self) -> None:
        stack = Stack(2)
        stack.push(0)
        stack.push(1)
        self.assertEqual(stack.size(), 2)

    def test_init(self) -> None:
        s1 = Stack(5)
        self.assertEqual(s1.capacity, 5)
        self.assertEqual(s1.num_items, 0)
        self.assertNotEqual(s1.capacity, 0)
        self.assertNotEqual(s1.num_items, 1)

    def test_is_empty(self) -> None:
        s1 = Stack(2)
        s1.push(10)
        s2 = Stack(4)
        self.assertFalse(s1.is_empty())
        self.assertTrue(s2.is_empty())

    def test_is_full(self) -> None:
        s1 = Stack(2)
        s1.push(10)
        s1.push(2)
        s2 = Stack(4)
        self.assertTrue(s1.is_full())
        self.assertFalse(s2.is_full())

    def test_push(self) -> None:
        s1 = Stack(3)
        s1.push(1)
        s1.push(2)
        s1.push(3)
        self.assertEqual(s1.peek(), 3)
        with self.assertRaises(IndexError):
            s1.push(2)

    def test_pop(self) -> None:
        s1 = Stack(4)
        s1.push(10)
        s1.push(2)
        self.assertEqual(s1.pop(), 2)
        self.assertEqual(s1.num_items, 1)

    def test_pop_idx_error(self) -> None:
        s1 = Stack(3)
        with self.assertRaises(IndexError):
            s1.pop()

    def test_peek(self) -> None:
        s1 = Stack(4)
        s1.push(10)
        s1.push(2)
        self.assertEqual(s1.peek(), 2)
        self.assertEqual(s1.num_items, 2)

    def test_peek_idx_error(self) -> None:
        with self.assertRaises(IndexError):
            Stack(4).peek()
        with self.assertRaises(IndexError):
            Stack(12).peek()

    def test_size(self) -> None:
        s1 = Stack(4)
        s1.push(10)
        s1.push(2)
        self.assertEqual(s1.size(), 2)


if __name__ == '__main__': 
    unittest.main()

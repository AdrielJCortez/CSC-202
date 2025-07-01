import unittest
from binary_search_tree import *
# adding this just so I can commit and push again (mine didn't get graded from the first autograder wave)
class TestLab5(unittest.TestCase):

    # Trivial Test
    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.inorder_list(), [])
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(3)
        bst.insert(5)
        bst.insert(2)
        bst.insert(1)
        bst.insert(10)
        bst.insert(11)
        bst.insert(4)
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (1, None))
        self.assertEqual(bst.tree_height(), 3)
        self.assertEqual(bst.inorder_list(), [1, 2, 3, 4, 5, 10, 11])
        self.assertEqual(bst.preorder_list(), [3, 2, 1, 5,4,  10, 11])
        self.assertEqual(bst.level_order_list(), [3, 2, 5, 1, 4, 10, 11])

    def test_is_empty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst2 = BinarySearchTree()
        bst2.insert(1)
        self.assertFalse(bst2.is_empty())

    def test_search_insert_max_min(self):
        bst = BinarySearchTree()
        bst2 = BinarySearchTree()
        bst.insert(3)
        bst.insert(5)
        bst.insert(2)
        bst.insert(1)
        bst.insert(10)
        bst.insert(11)
        bst.insert(4)
        self.assertTrue(bst.search(1))
        self.assertTrue(bst.search(3))
        self.assertTrue(bst.search(11))
        self.assertFalse(bst.search(12))
        self.assertFalse(bst.search(0))
        self.assertEqual(bst2.find_min(), None)
        self.assertEqual(bst.find_min(), (1, None))
        self.assertEqual(bst2.find_max(), None)
        self.assertEqual(bst.find_max(), (11, None))
        self.assertEqual(bst2.tree_height(), None)
        self.assertEqual(bst.tree_height(), 3)

    def test_list(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])
        self.assertFalse(bst.search(1))

    def test(self):
        bst = BinarySearchTree()
        bst.insert(4)
        bst.insert(3)
        bst.insert(2)
        bst.insert(1)
        self.assertEqual(bst.tree_height(), 3)




if __name__ == '__main__': 
    unittest.main()

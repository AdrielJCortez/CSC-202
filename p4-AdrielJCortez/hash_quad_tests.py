import unittest
from hash_quad import *


class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0)  # Causes rehash
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def test(self):
        ht = HashTable(10)
        ht.insert("catapult", 5)
        ht.insert("catapulted", 4)
        ht.insert("catapults", 6)
        self.assertEqual(ht.get_all_keys(), ["catapult", "catapulted", "catapults"])
        self.assertEqual(ht.get_index("catapulted"), 1)
        self.assertEqual(ht.get_index("catapult"), 0)
        self.assertEqual(ht.get_index("catapults"), 4)
        self.assertFalse(ht.in_table("catapultts"))
        self.assertEqual(ht.get_value("catapultts"), None)
        self.assertEqual(ht.get_value("catapults"), 6)

    def test_8_or_larger(self):
        ht = HashTable(191)
        ht.insert("catapult", 5)
        ht.insert("catapulted", 4)
        ht.insert("catapults", 6)
        ht.insert("catapult", 5)
        ht.insert("catapult", 9)
        self.assertEqual(ht.get_value("catapult"), 9)
        self.assertEqual(ht.get_value("catapults"), 6)
        self.assertEqual(ht.get_all_keys(), ['catapult', 'catapulted', 'catapults'])

    def test_retrieve_from_empty(self):
        ht = HashTable(5)
        self.assertEqual(ht.get_value("cat"), None)
        self.assertEqual(ht.get_index("Cat"), None)

    def test_small_hash_tables(self):
        ht1 = HashTable(1)
        ht2 = HashTable(3)
        ht3 = HashTable(-2)
        self.assertEqual(ht1.table_size, 2)
        self.assertEqual(ht2.table_size, 3)
        self.assertEqual(ht3.table_size, 2)


if __name__ == '__main__':
    unittest.main()

import unittest
import subprocess
from concordance import *


class TestList(unittest.TestCase):

    def test_01(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("diff -wb file1_con.txt file1_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_02(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("diff -wb file2_con.txt file2_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_03(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_empty(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("empty_file.txt")
        conc.write_concordance("empty_file_con.txt")
        err = subprocess.call("diff -wb empty_file_con.txt empty_file_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_symbols(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("symbols_file.txt")
        conc.write_concordance("symbols_file_con.txt")
        err = subprocess.call("diff -wb symbols_file_con.txt symbols_file_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_all_nums(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("nums_file.txt")
        conc.write_concordance("nums_file_con.txt")
        err = subprocess.call("diff -wb nums_file_con.txt nums_file_sol.txt", shell=True)
        self.assertEqual(err, 0)

    def test_fnf(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_stop_table("hi")

    def test_fnf2(self):
        conc = Concordance()
        with self.assertRaises(FileNotFoundError):
            conc.load_concordance_table("joe")


if __name__ == '__main__':
    unittest.main()

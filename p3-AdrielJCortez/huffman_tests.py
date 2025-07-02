import unittest
import subprocess
from ordered_list import *
from huffman import *


class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_lt_and_eq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        ascii = 97
        lst = OrderedList()
        for freq in anslist:
            node = HuffmanNode(ascii, freq)
            lst.add(node)
            ascii += 1
        self.assertEqual(lst.index(HuffmanNode(101, 0)), 0)
        self.assertEqual(lst.index(HuffmanNode(100, 16)), 6)
        self.assertEqual(lst.index(HuffmanNode(97, 2)), 2)
        self.assertFalse(HuffmanNode(97, 2) == None)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')
        self.assertEqual(codes[ord('z')], '')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        self.assertEqual(subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell=True), 0)
        self.assertEqual(subprocess.call("diff -wb file1_out_compressed.txt file1_compressed_soln.txt", shell=True), 0)

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        self.assertEqual(subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell=True), 0)
        self.assertEqual(subprocess.call("diff -wb file2_out_compressed.txt file2_compressed_soln.txt", shell=True), 0)

    def test_03_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        self.assertEqual(subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell=True), 0)
        self.assertEqual(
            subprocess.call("diff -wb declaration_out_compressed.txt declaration_compressed_soln.txt", shell=True), 0)

    def test_04_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        self.assertEqual(subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell=True), 0)
        self.assertEqual(
            subprocess.call("diff -wb multiline_out_compressed.txt multiline_compressed_soln.txt", shell=True), 0)

    def test_single_textfile(self):
        huffman_encode("single_char.txt", "single_char_out.txt")
        self.assertEqual(subprocess.call("diff -wb single_char_out.txt single_char_soln.txt", shell=True), 0)

    def test_empty_file(self):
        # Encode the empty file
        output_file = "empty_file_encoded.txt"
        huffman_encode("empty_file.txt", output_file)

        # Open the output file and check if it's empty
        with open(output_file, "r") as file:
            encoded_content = file.read()
            self.assertEqual(encoded_content, "")

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            huffman_encode("hi.txt", "hi_out.txt")

    def test_01a_test_file1_parse_header(self):
        f = HuffmanBitReader('file1_compressed_soln.txt')
        header = f.read_str()
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3,
                    0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)

    def test_01_test_file_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)

    def test_02_test_file_decode(self):
        huffman_decode("empty_file_compressed_soln.txt", "empty_file_decoded.txt")
        err = subprocess.call("diff -wb empty_file.txt empty_file_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_03_test_file_decode(self):
        huffman_decode("single_char_compressed_soln.txt", "single_char_decoded.txt")
        err = subprocess.call("diff -wb single_char.txt single_char_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_04_test_file_decode(self):
        huffman_decode("declaration_compressed_soln.txt", "declaration_decoded.txt")
        err = subprocess.call("diff -wb declaration.txt declaration_decoded.txt", shell=True)
        self.assertEqual(err, 0)

    def test_05_test_file_decode(self):
        with self.assertRaises(FileNotFoundError):
            huffman_decode("does_not_exist_compressed_soln.txt", "does_not_exist_decoded.txt")


if __name__ == '__main__':
    unittest.main()

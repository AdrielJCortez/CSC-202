import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base0(self) -> None:
        with self.assertRaises(ValueError):
            convert(0, 0)

    def test_base2(self) -> None:
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self) -> None:
        self.assertEqual(convert(30,4),"132")

    def test_base16(self) -> None:
        self.assertEqual(convert(316,16),"13C")


if __name__ == "__main__":
        unittest.main()

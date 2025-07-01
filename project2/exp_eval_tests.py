# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_00(self) -> None:
        self.assertAlmostEqual(postfix_eval("2.1 56 48 - 2 / 3 + 6 * +"), 44.1)

    def test_postfix_eval_01(self) -> None:
        self.assertAlmostEqual(postfix_eval("3  5 +"), 8)

    def test_postfix_eval_02(self) -> None:
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self) -> None:
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self) -> None:
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self) -> None:
        self.assertAlmostEqual(postfix_eval("2 56 48 - 2 / 3 + 6 * +"), 44)

    def test_postfix_eval_06(self) -> None:
        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("3 3 / 1 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_07(self) -> None:
        try:
            postfix_eval("")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Empty input")

    def test_postfix_eval_08(self) -> None:
        with self.assertRaises(ValueError):
            postfix_eval("1 0 / 1 +")

    def test_postfix_eval_09(self) -> None:
        self.assertEqual(postfix_eval("1 0 + 1 >>"), 0)
        self.assertEqual(postfix_eval("1 0 + 1 <<"), 2)

    def test_postfix_eval_11(self):
        try:
            postfix_eval("3.0 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_10(self) -> None:
        self.assertEqual(postfix_eval("3 2 **"), 9)
        with self.assertRaises(ValueError):
            postfix_eval(
                "12 1.2 * 10 10 - / 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 10 / 9 / 2.8 * 3 - 6.2 "
                "4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")

    def test_infix_to_postfix_01(self) -> None:
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual("3 4 2 * 1 5 - 2 3 ** ** / +", infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"))
        self.assertEqual("3 4 2 * 1 5 - 2 3 ** ** / +", infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"))
        self.assertEqual(infix_to_postfix("5 + 2 ** 1 >> 4"), "5 2 1 4 >> ** +")

    def test_infix_to_postfix_02(self) -> None:
        self.assertEqual(infix_to_postfix("2 + ( ( 56 - 48 ) / 2 + 3 ) * 7"), "2 56 48 - 2 / 3 + 7 * +")

    def test_infix_to_postfix_03(self) -> None:
        self.assertEqual(infix_to_postfix("5 + ( 1 ** 2 ) - ( 6 * 5 ( 6 / 3 ) ) >> 2"), "5 1 2 ** + 6 5 6 3 / * 2 >> -")

    def test_prefix_to_postfix(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

    def test_prefix_to_postfix2(self) -> None:
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 + / 4 5 6"), "3 2 1 / - 4 5 / 6 + *")

    def test_prefix_to_postfix3(self) -> None:
        self.assertEqual(prefix_to_postfix("+ 3 4"), "3 4 +")
        self.assertEqual(prefix_to_postfix("* + 5 4 - 6 2"), "5 4 + 6 2 - *")
        self.assertEqual(prefix_to_postfix("** 2 3"), "2 3 **")
        self.assertEqual(prefix_to_postfix(">> 4 1"), "4 1 >>")
        self.assertEqual(prefix_to_postfix("+ * 3 4 ** 2 3"), "3 4 * 2 3 ** +")
        self.assertEqual(prefix_to_postfix("+ 10 * 5 4"), "10 5 4 * +")
        self.assertEqual(prefix_to_postfix("+ 10 * 5 4"), "10 5 4 * +")
        self.assertEqual(prefix_to_postfix("- 0 5"), "0 5 -")
        self.assertEqual(prefix_to_postfix("/ 10 2"), "10 2 /")
        self.assertEqual(prefix_to_postfix("+ 3.0 4.0"), "3.0 4.0 +")

    def test_infix_to_postfix3(self) -> None:
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("1 + 2 * 3 - 4 / 5 ** 6"), "1 2 3 * + 4 5 6 ** / -")
        self.assertEqual(infix_to_postfix("( 3 + 4 ) * 5"), "3 4 + 5 *")
        self.assertEqual(infix_to_postfix("2 + 3 * 4"), "2 3 4 * +")

    def test_prefix_to_postfix_eval_post(self) -> None:
        x = prefix_to_postfix("* - 3 / 2 1 - / 4 5 6")
        self.assertAlmostEqual(postfix_eval(x), -(26 / 5))

    def test_prefix_to_postfix_eval_post02(self) -> None:
        y = prefix_to_postfix("* - 3 / 2 1 + / 4 5 6")
        self.assertEqual(postfix_eval(y), (34 / 5))

    def test_postfix_eval12(self):
        with self.assertRaises(ValueError):
            postfix_eval("1 0 /")

    def test_postfix(self):
        with self.assertRaises(ValueError):
            postfix_eval("12 1.2 * 10 10 - / 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 10 / 9 / 2.8 "
                         "* 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")


if __name__ == "__main__":
    unittest.main()

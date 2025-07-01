import unittest
import perm_lex

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])

    def test_perm_gen_lex2(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

    def test_perm_gen_lex3(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex(""), [])

    def test_perm_gen_lex4(self) -> None:
        self.assertEqual(perm_lex.perm_gen_lex("a"), ["a"])


if __name__ == "__main__":
        unittest.main()

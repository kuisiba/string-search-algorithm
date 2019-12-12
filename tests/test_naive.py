import unittest

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
import naive 

class TestNaive(unittest.TestCase):
    def test1(self):
        str = "abcde"
        substr = "ab"
        ret = naive.naive(str, substr)
        self.assertEqual(ret, 0)
    def test2(self):
        str = "abcde"
        substr = "bc"
        ret = naive.naive(str, substr)
        self.assertEqual(ret, 1)
    def test3(self):
        str = "aaaaaaaaaab"
        substr = "ab"
        ret = naive.naive(str, substr)
        self.assertEqual(ret, 9)
    def test4(self):
        str = "あいうえお"
        substr = "う"
        ret = naive.naive(str, substr)
        self.assertEqual(ret, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest

from InvertBinaryTree import Solution

class Test(unittest.TestCase):

    def test_result(self):
        self.assertEqual(Solution.invertTree(self,[4,2,7,1,3,6,9]),[4,7,2,9,6,3,1])

if __name__ == '__main__':
    unittest.main()
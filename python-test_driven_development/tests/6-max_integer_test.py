""" Unittest for max_integer function """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list(self):
        self.assertEqual(max_integer([32, 12, 74, 12]), 74)

    def test_max_at_beginning_list(self):
        self.assertEqual(max_integer([42, 2, 7, 12]), 42)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_strings_list(self):
        self.assertEqual(max_integer(['Hello', 'World']), 'World')

    def test_one_item_list(self):
        self.assertEqual(max_integer([12]), 12)

if __name__ == '__main__':
    unittest.main()
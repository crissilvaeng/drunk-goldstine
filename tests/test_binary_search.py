import unittest

from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_invalid_elements(self):
        with self.assertRaises(ValueError):
            binary_search([], 42)

    def test_binary_search_invalid_element(self):
        with self.assertRaises(ValueError):
            binary_search([42], None)


if __name__ == '__main__':
    unittest.main()

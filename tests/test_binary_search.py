import unittest

from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_search_with_invalid_elements(self):
        with self.assertRaises(ValueError):
            binary_search([], 42)

    def test_search_with_invalid_element(self):
        with self.assertRaises(ValueError):
            binary_search([42], None)

    def test_search_single_item_in_element(self):
        self.assertEquals(0, binary_search([42], 42))

    def test_search_even_items_in_list(self):
        self.assertEquals(0, binary_search([1, 2, 3, 4], 1))

    def test_search_odd_items_in_list(self):
        self.assertEquals(0, binary_search([1, 2, 3, 4, 5], 1))

    def test_search_absent_element_in_list(self):
        self.assertEquals(-1, binary_search([1, 2, 3, 4, 5], 42))

    def test_search_with_strings(self):
        self.assertEquals(0, binary_search(
            ['Alpha', 'Bravo', 'Charlie'], 'Alpha'))

    def test_search_with_chars(self):
        self.assertEquals(3, binary_search('Charlie', 'r'))

    def test_search_elements_and_element_different_types(self):
        with self.assertRaises(TypeError):
            self.assertEquals(0, binary_search([1, 2, 3], 'Zulu'))


if __name__ == '__main__':
    unittest.main()

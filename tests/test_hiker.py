import unittest

from src.hiker import global_answer, Hiker


class TestHiker(unittest.TestCase):

    def test_global_function(self):
        self.assertEqual(42, global_answer())

    def test_instance_method(self):
        self.assertEqual(42, Hiker().instance_answer())


if __name__ == '__main__':
    unittest.main()

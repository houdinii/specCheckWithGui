import unittest
from spec_checker.modules.utilities import truncate, get_size


class UtilitiesTest(unittest.TestCase):
    """Tests the utilities module"""
    def test_get_size_function(self):
        """Tests the get_size function for proper values"""
        self.assertEqual(get_size(1253656), "1.20MB", "get_size should output properly formatted and correct values")
        self.assertEqual(get_size(1253656678), "1.17GB", "get_size should output properly formatted and correct values")

    def test_truncate_function(self):
        """Tests the truncate function for proper values"""
        self.assertEqual(truncate(12.3456789, 2), "12.34", "truncate should output properly formatted and correct values")
        self.assertEqual(truncate(12.3456789, 5), "12.34567", "truncate should output properly formatted and correct values")


if __name__ == "__main__":
    unittest.main()

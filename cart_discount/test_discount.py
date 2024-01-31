import unittest 
from unittest import TestCase
from price_discount import discount  


class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    def test_list_with_four_prices(self):
        prices = [20, 3, 9, 15]
        expected_discount = 3
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_two_prices(self):
        prices = [10, 4]
        expected_discount = 0
        self.assertEqual(expected_discount, discount(prices))

    def test_list_of_floats(self):
        prices = [10.56, 12.8, 1.23]
        expected_discount = 1.23
        self.assertEqual(expected_discount, discount(prices))

    def test_empty_list(self):
        prices = []
        self.fail("finish this test")

    def test_list_of_strings(self):
        prices = ["one", "two", "three"]
        self.fail("finish this test")


if __name__ == '__main__':
    unittest.main()
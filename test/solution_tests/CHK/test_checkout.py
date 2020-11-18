import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_single_item(self):
        self.assertEqual(checkout("A"), 50)

    def test_bad_input(self):
        self.assertEqual(checkout(-1), -1)

    def test_bad_input_string(self):
        self.assertEqual(checkout("*"), -1)

    def test_empty_input_string(self):
        self.assertEqual(checkout(""), 0)

    def test_multiple_items(self):
        self.assertEqual(checkout("ABCD"), 115)

    def test_special_offers(self):
        self.assertEqual(checkout("AAA"), 130)

    def test_multiple_special_offers(self):
        self.assertEqual(checkout("AAABB"), 175)

    def test_special_offers_plus_one(self):
        self.assertEqual(checkout("AAAA"), 180)

    def test_special_offer_b(self):
        self.assertEqual(checkout("BB"), 45)

    def test_special_offer_e_and_b(self):
        self.assertEqual(checkout("EEB"), 80)

    def test_special_offer_e_and_b2(self):
        self.assertEqual(checkout("BBEE"), 110)

    def test_special_offer_six_a(self):
        self.assertEqual(checkout("AAAAAA"), 250)


if __name__ == "__main__":
    unittest.main()

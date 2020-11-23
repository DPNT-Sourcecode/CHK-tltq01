import unittest
from lib.solutions.CHK.checkout_solution import checkout, load_table


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

    def test_special_offer_one_f(self):
        self.assertEqual(checkout("F"), 10)

    def test_special_offer_two_f(self):
        self.assertEqual(checkout("FF"), 20)

    def test_special_offer_three_f(self):
        self.assertEqual(checkout("FFF"), 20)


class TestLoadTable(unittest.TestCase):
    def test_load_table_not_none(self):
        self.assertIsNotNone(load_table(
            'C:\\Dev\\Python\\i3verticals\\accelerate_runner\\db\\items.json'))

    def test_load_table_is_dict(self):
        d = load_table(
            'C:\\Dev\\Python\\i3verticals\\accelerate_runner\\db\\discounts.json')
        self.assertDictContainsSubset(
            {'amount': 20, 'itemId': 'A', 'item_to_discount': 'A', 'quantity': 3}, d[0])


if __name__ == "__main__":
    unittest.main()




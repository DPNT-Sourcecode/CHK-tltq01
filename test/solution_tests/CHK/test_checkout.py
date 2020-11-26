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

    def test_special_offer_three_f(self):
        self.assertEqual(checkout("FFF"), 20)

# 5H for 45
    def test_special_offer_five_h(self):
        self.assertEqual(checkout("HHHHH"), 45)

# 10H for 80
    def test_special_offer_ten_h(self):
        self.assertEqual(checkout("HHHHHHHHHH"), 80)

# 2K for 150
    def test_special_offer_2_k(self):
        self.assertEqual(checkout("KK"), 150)

# 3N get one M free
    def test_special_offer_three_n(self):
        self.assertEqual(checkout("NNN"), 120)

    def test_special_offer_three_n_discount_m(self):
        self.assertEqual(checkout("NNNM"), 120)

# 5P for 200
    def test_special_offer_five_p(self):
        self.assertEqual(checkout("PPPPP"), 200)


# 3Q for 80

    def test_special_offer_three_q(self):
        self.assertEqual(checkout("QQQ"), 80)


# 3R get one Q free

    def test_special_offer_three_r(self):
        self.assertEqual(checkout("RRR"), 150)

    def test_special_offer_three_r_discount_q(self):
        self.assertEqual(checkout("RRRQ"), 150)


# 3U get one U free

    def test_special_offer_three_u(self):
        self.assertEqual(checkout("UUU"), 120)

    def test_special_offer_four_u_discount(self):
        self.assertEqual(checkout("UUUU"), 120)


# 2V for 90

    def test_special_offer_two_v(self):
        self.assertEqual(checkout("VV"), 90)


# 3V for 130

    def test_special_offer_three_v(self):
        self.assertEqual(checkout("VVV"), 130)

    def test_special_offer_a_to_z(self):
        self.assertEqual(checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), 965)


class TestLoadTable(unittest.TestCase):
    def test_load_table_not_none(self):
        self.assertIsNotNone(load_table(
            'db\\items.json'))

    def test_load_table_is_dict(self):
        d = load_table(
            'db\\discounts.json')
        self.assertDictContainsSubset(
            {"amount": 20, "discounted_items": ["A"], "discount_type": "basic", "item_list": ["A"], "quantity": 3}, d[0])


if __name__ == "__main__":
    unittest.main()





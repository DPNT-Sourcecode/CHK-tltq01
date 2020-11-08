import unittest
from lib.solutions.CHK.checkout_solution import checkout


class TestCheckout(unittest.TestCase):
    def test_single_item(self):
        self.assertEqual(checkout("A"), 50)


if __name__ == "__main__":
    unittest.main()

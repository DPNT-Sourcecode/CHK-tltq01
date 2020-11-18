# Item	Price
# A	50
# B	30
# C	20
# D	15
# E	40

# Item	Quantity	Discount	ItemToDiscount
# A	3	20	A
# A	5	50	A
# B	2	15	B
# E	2	30	B


prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

special_offers = [
    {"priority": 1, "eligible_item": "E", "quantity": 2,
        "discount": 30, "item_to_discount": "B"},
    {"priority": 2, "eligible_item": "A", "quantity": 5,
        "discount": 50, "item_to_discount": "A"},
    {"priority": 3, "eligible_item": "A", "quantity": 3,
        "discount": 20, "item_to_discount": "A"},
    {"priority": 4, "eligible_item": "B", "quantity": 2,
        "discount": 15, "item_to_discount": "B"}
]


class LineItem:
    def __init__(self, item, price, count):
        self.item = item
        self.price = price
        self.count = count
        self.discount = 0

    def subtotal(self):
        return self.price * self.count - self.discount


def prepare_cart(skus: str) -> dict:
    cart = dict()
    for s in skus:
        if s not in cart:
            cart[s] = 1
    else:
        cart[s] += 1

    for item in prices.keys():
        subtotals[item] = prices[item] * \
            cart[item] if item in cart.keys() else 0

    return cart


def get_max_discount(cart: dict) -> int:
    best_discount = -1

    if "E" in cart.keys() and cart["E"] > 2 and "B" in cart.keys() and cart["B"] > 0:

    for offer in sorted(special_offers, key=lambda offer: offer["priority"]):
        item = offer["eligible_item"]
        if item in cart.keys() and cart[item] >= offer["quantity"]:
            discounted_item = offer["item_to_discount"]
            if discounted_item == item:
                pass
            else:
                if discounted_item in cart.keys() and cart[discounted_item] > 1:
                    pass

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    try:
        cart = prepare_cart(skus)

        subtotals = get_item_subtotals(cart)

        max_discount = get_max_discount(cart)

        return total - max_discount
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEE"))

    # for item in special_offers.keys():
    #     # Sort discounts by the greatest amount saved first
    #     for offer in sorted(special_offers[item], key=lambda discount: discount["priority"]):
    #         while True:
    #             # if discount available and conditions met, add item-prices to total and apply discount
    #             # "EEB"
    #             if item in cart.keys() and cart[item] >= offer["quantity"]:
    #                 subtotal = prices[item] * offer["quantity"]  # 2E * 40
    #                 cart[item] -= offer["quantity"]  # "B"

    #                 if item == offer["item_to_discount"]:
    #                     subtotal -= offer["discount"]
    #                 elif offer["item_to_discount"] in cart.keys() and cart[offer["item_to_discount"]] > 0:

    #                 total += subtotal
    #             else:
    #                 break

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


def get_item_counts(cart: str) -> dict:
    """count the numer of each item in the cart"""
    items = dict()
    for s in cart:
        if s not in items:
            items[s] = 1
    else:
        items[s] += 1

    return items


def get_item_subtotals(cart: dict) -> dict:
    subtotals = {}

    for item in prices.keys():
        subtotals[item] = prices[item] * \
            cart[item] if item in cart.keys() else 0

    return subtotals


def get_max_discount(cart: dict) -> int:
    best_discount = -1

    for offer in sorted(special_offers, key=lambda offer: offer["priority"]):

        # discounts = dict()
        # for item in cart.keys():
        #     subtotal = 0
        #     if item in special_offers.keys():
        #         for offer in sorted(special_offers[item], key=lambda discount: discount["priority"]):
        #             if cart[item] >= offer["quantity"]:
        #                 subtotal += prices[item] * offer["quantity"]
        #                 cart[item] -= offer["quantity"]

        #                 if item == offer["item_to_discount"]:
        #                     subtotal -= offer["discount"]
        #                 elif offer["item_to_discount"] in cart.keys() and cart[offer["item_to_discount"]] > 0:
        #                     # What if B's have already been counted!?
        #                     cart[offer["item_to_discount"]] -= 1

        # return sum(discounts.values())

        # noinspection PyUnusedLocal
        # skus = unicode string


def checkout(skus: str):
    try:
        cart = get_item_counts(skus)

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





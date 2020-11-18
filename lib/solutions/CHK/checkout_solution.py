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

special_offers = {
    "A": [
        {"priority": 1, "quantity": 3, "discount": 20, "item_to_Discount": "A"},
        {"priority": 2, "quantity": 5, "discount": 50, "item_to_Discount": "A"}
    ],
    "B": [
        {"priority": 1, "quantity": 2, "discount": 15, "item_to_Discount": "B"}
    ],
    "E": [
        {"priority": 1, "quantity": 2, "discount": 30, "item_to_Discount": "B"}
    ]
}


def get_item_counts(cart: str) -> dict:
    """count the numer of each item in the cart"""
    items = dict()
    for s in cart:
        if s not in items:
            items[s] = 1
    else:
        items[s] += 1

    return items


def get_cart_total(cart: dict) -> int:
    total = 0
    for item in cart.keys():
        total += cart[item] * prices[item]

    return total


def get_max_discount(cart: dict) -> int:
    discounts = dict()

    for item in cart.keys():

        # noinspection PyUnusedLocal
        # skus = unicode string


def checkout(skus: str):
    try:
        cart = get_item_counts(skus)

        total = get_cart_total(cart)

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

    #                 if item == offer["item_to_Discount"]:
    #                     subtotal -= offer["discount"]
    #                 elif offer["item_to_Discount"] in cart.keys() and cart[offer["item_to_Discount"]] > 0:

    #                 total += subtotal
    #             else:
    #                 break




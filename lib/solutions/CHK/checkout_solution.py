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


def get_item_counts(cart):
    """count the numer of each item in the cart"""
    items = dict()
    for s in items:
        if s not in items:
            items[s] = 1
    else:
        items[s] += 1

    return items

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    cart = {}
    total = 0

    try:
        cart = get_item_counts(skus)
        # handle special offers first, if there are enough of the given item
        for item in special_offers.keys():
            # Sort discounts by the greatest amount saved first
            for offer in sorted(special_offers[item], key=lambda discount: discount[0]):
                while True:
                    # if discount available and conditions met, add item-prices to total and apply discount
                    if item in cart.keys() and cart[item] >= offer["quantity"]:
                        subtotal = prices[item] * \
                            offer["quantity"] - offer["discount"]
                        total += special_offers[item]["discount"]
                        cart[item] -= special_offers[item]["quantity"]
                    else:
                        break

        # add the prices of the rest of the items to the final total
        for item in cart.keys():
            total += cart[item] * prices[item]

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("A"))







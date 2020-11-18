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
    "E": {"quantity": 2, "discount": 30, "item_to_discount": "B"},
    "A": {"quantity": 5, "discount": 50, "item_to_discount": "A"},
    "A": {"quantity": 3, "discount": 20, "item_to_discount": "A"},
    "B": {"quantity": 2, "discount": 15, "item_to_discount": "B"}
}


# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    cart = {}
    total = 0

    try:
        for p in prices.keys():
            cart.setdefault(p, 0)

        for s in skus:
            cart[s] += 1

        for item in special_offers.keys():
            offer = special_offers[item]

            while cart[item] >= offer["quantity"]:
                if offer["item_to_discount"] == item:
                    cart[item] -= offer["quantity"]
                    total += (prices[item] *
                              offer["quantity"]) - offer["discount"]
                elif cart[offer["item_to_discount"]] > 0:
                    cart[item] -= offer["quantity"]
                    total += (prices[item] * offer["quantity"])
                    cart[offer["item_to_discount"]] -= 1

        for item in cart.keys():
            total += cart[item] * prices[item]

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEE"))


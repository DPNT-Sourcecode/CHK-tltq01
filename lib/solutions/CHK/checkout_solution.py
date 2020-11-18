
prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

special_offers = [
    {"item": "E", "quantity": 2, "discount": 30, "item_to_discount": "B"},
    {"item": "A", "quantity": 5, "discount": 50, "item_to_discount": "A"},
    {"item": "A", "quantity": 3, "discount": 20, "item_to_discount": "A"},
    {"item": "B", "quantity": 2, "discount": 15, "item_to_discount": "B"}
]

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

        for offer in special_offers:
            item = offer["item"]

            while cart[item] >= offer["quantity"]:
                if offer["item_to_discount"] == item:
                    cart[item] -= offer["quantity"]
                    total += (prices[item] *
                              offer["quantity"]) - offer["discount"]
                elif cart[offer["item_to_discount"]] > 0:
                    cart[item] -= offer["quantity"]
                    total += (prices[item] * offer["quantity"])

                    cart[offer["item_to_discount"]] -= 1
                    total += (prices[offer["item_to_discount"]
                                     ] - offer["discount"])

        for item in cart.keys():
            total += cart[item] * prices[item]

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEE"))




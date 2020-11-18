
prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40
}

special_offers = [
    # item, quantity, discount, item_to_discount
    ["A", 5, 50, "A"],
    ["E", 2, 30, "B"],
    ["A", 3, 20, "A"],
    ["B", 2, 15, "B"]
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

        for offer in sorted(special_offers, lambda offer: offer[2], reverse=True):
            item, quantity, discount, item_to_discount = offer

            while cart[item] >= quantity:
                if item_to_discount == item:
                    cart[item] -= quantity
                    total += (prices[item] *
                              quantity) - discount
                elif cart[item_to_discount] > 0:
                    cart[item] -= quantity
                    total += (prices[item] * quantity)

                    cart[item_to_discount] -= 1
                    total += (prices[item_to_discount] - discount)

        for item in cart.keys():
            total += cart[item] * prices[item]

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEE"))







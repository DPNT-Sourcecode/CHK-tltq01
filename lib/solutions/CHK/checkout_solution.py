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


# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    cart = {}

    try:
        for p in prices.keys():
            cart.setdefault(p, 0)

        for s in skus:
            cart[s] += 1

    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEE"))




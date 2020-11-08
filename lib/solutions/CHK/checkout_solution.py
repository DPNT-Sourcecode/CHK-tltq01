prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

special_offers = {
    "A": (3, 130),
    "B": (2, 45)
}

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    cart = {}

    for s in skus:
        if s not in cart:
            cart[s] = 1
        else:
            cart[s] += 1



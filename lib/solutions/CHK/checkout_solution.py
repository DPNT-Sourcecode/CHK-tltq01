prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}

special_offers = {
    "A": {
        "qty": 3,
        "price": 130
    },
    "B": {
        "qty": 2,
        "price": 45
    }
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

    total = 0

    for item in special_offers.keys:
        while True:
            if item in cart.keys and cart[item] >= special_offers[item]["qty"]:
                total += special_offers[item]["price"]
                cart[item] -= special_offers[item]["qty"]
            else:
                break





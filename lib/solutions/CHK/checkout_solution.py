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

    # count the numer of each item in the cart
    for s in skus:
        if s not in cart:
            cart[s] = 1
        else:
            cart[s] += 1

    total = 0

    # handle special offers first, if there are enough of the given item
    for item in special_offers.keys():
        while True:
            if item in cart.keys() and cart[item] >= special_offers[item]["qty"]:
                total += special_offers[item]["price"]
                cart[item] -= special_offers[item]["qty"]
            else:
                break

    # add the prices of the rest of the items to the final total
    for item in cart.keys():
        total += cart[item] * prices[item]

    return total


if __name__ == "__main__":
    print(checkout("A"))

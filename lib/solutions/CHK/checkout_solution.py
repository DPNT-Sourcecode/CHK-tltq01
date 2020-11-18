import Counter

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
        {"quantity": 3, "discount": 20, "item_to_Discount": "A"},
        {"quantity": 5, "discount": 50, "item_to_Discount": "A"}
    ],
    "B": [
        {"quantity": 2, "discount": 15, "item_to_Discount": "B"}
    ],
    "E": [
        {"quantity": 2, "discount": 30, "item_to_Discount": "B"}
    ]
}

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    cart = {}
    total = 0

    try:
        # count the numer of each item in the cart
        for s in skus:
            if s not in cart:
                cart[s] = 1
            else:
                cart[s] += 1

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
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("A"))


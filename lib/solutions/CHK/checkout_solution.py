import json
from os import path
from models.price import Price

root = 'C:\\Dev\\Python\\i3verticals\\accelerate_runner'


def load_table(file_path: str) -> dict:
    data = None
    abs_path = path.join(root, file_path)

    with open(abs_path, 'r') as file:
        data = json.load(file)

    return data


def load_prices() -> list:
    data = load_table('db\\items.json')
    prices = []
    for d in data:
        p = Price()
        p.itemId = d["itemId"]
        p.price = d["price"]
        prices.append(p)

    return prices

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    cart = {}
    total = 0

    try:
        prices = load_prices()
        discounts = load_table('db\\discounts.json')

        for p in prices.keys():
            cart.setdefault(p, 0)

        # build the cart
        for s in skus:
            cart[s] += 1

        # ensure we're handling the best discounts first
        for offer in sorted(discounts, key=lambda offer: offer[2], reverse=True):
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
                else:
                    break

        # total remaining items after discounts
        for item in cart.keys():
            total += cart[item] * prices[item]

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEEFFF"))








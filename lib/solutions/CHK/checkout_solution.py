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
        p.item_id = d["item_id"]
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
            item_id, quantity, discount, discounted_item_id = offer
            item = filter(lambda p: p.item_id == item_id, prices)
            discounted_item = filter(
                lambda p: p.item_id == discounted_item_id, prices)

            while cart[item_id] >= quantity:
                if discounted_item_id == item_id:
                    cart[item_id] -= quantity
                    total += (item.price *
                              quantity) - discount
                elif cart[discounted_item_id] > 0:
                    cart[item_id] -= quantity
                    total += (item.price * quantity)

                    cart[discounted_item_id] -= 1
                    total += (discounted_item.price - discount)
                else:
                    break

        # total remaining items after discounts
        for item_id in cart.keys():
            total += cart[item_id] * item.price

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEEFFF"))










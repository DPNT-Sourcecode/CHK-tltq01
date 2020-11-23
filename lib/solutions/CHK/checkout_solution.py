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
        p = Price(d["item_id"], int(d["price"]))
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

        # build the cart
        for s in skus:
            if s not in cart.keys():
                cart.setdefault(s, 0)
            cart[s] += 1

        # ensure we're handling the best discounts first
        sorted_discounts = sorted(
            discounts, key=lambda offer: offer['amount'], reverse=True)
        for offer in sorted_discounts:
            amount, item_id, item_to_discount, quantity = offer
            item = filter(lambda p: p.item_id == item_id, prices)
            discounted_item = filter(
                lambda p: p.item_id == item_to_discount, prices)

            while cart[item_id] >= quantity:
                if item_to_discount == item_id:
                    cart[item_id] -= quantity
                    total += (item.price *
                              quantity) - amount
                elif cart[item_to_discount] > 0:
                    cart[item_id] -= quantity
                    total += (item.price * quantity)

                    cart[item_to_discount] -= 1
                    total += (discounted_item.price - amount)
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



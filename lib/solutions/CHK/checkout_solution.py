import json
from os import path


class Price:
    def __init__(self, item_id, price):
        self.item_id = item_id
        self.price = price


class Discount:
    def __init__(self, discount_type, item_list, quantity, amount, discounted_items):
        self.discount_type = discount_type
        self.item_list = item_list
        self.quantity = quantity
        self.amount = amount
        self.discounted_items = discounted_items


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


def load_discounts(cart) -> list:
    data = load_table('db\\discounts.json')
    discounts = []
    for d in data:
        p = Discount(d["discount_type"], d["item_list"], int(d["quantity"]),
                     int(d["amount"]), d["discounted_items"])

        # filter for only items in cart
        if p.item_id in cart:
            discounts.append(p)

    # ensure we're handling the best discounts first
    sorted_discounts = sorted(
        discounts, key=lambda d: d.amount, reverse=True)
    return sorted_discounts


def get_eligible_discounts(discounts: list, item_id: str) -> list:
    eligible_discounts = []

    return filter(lambda d: item_id in d.item_list, discounts)


# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    cart = {}
    total = 0

    try:
        prices = load_prices()

        # build the cart
        for s in skus:
            if s not in cart.keys():
                cart.setdefault(s, 0)
            cart[s] += 1

        discounts = load_discounts(cart.keys())

        for discount in discounts:
            item = next(
                filter(lambda p: p.item_id in discount.item_list, prices), None)

            discounted_item = next(filter(
                lambda p: p.item_id in discount.discounted_items, prices), None)

            if discount.item_id in cart.keys():
                while cart[discount.item_id] >= discount.quantity:
                    if discount.item_to_discount == discount.item_id:
                        cart[discount.item_id] -= discount.quantity
                        total += (item.price *
                                  discount.quantity) - discount.amount
                    elif discount.item_to_discount in cart.keys() and cart[discount.item_to_discount] > 0:
                        cart[discount.item_id] -= discount.quantity
                        total += (item.price * discount.quantity)

                        cart[discount.item_to_discount] -= 1
                        total += (discounted_item.price - discount.amount)
                    else:
                        break

        # total remaining items after discounts
        for item_id in cart.keys():
            item = next(filter(lambda p: p.item_id == item_id, prices), None)
            total += cart[item_id] * item.price

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("AAABBCDEEEFFF"))

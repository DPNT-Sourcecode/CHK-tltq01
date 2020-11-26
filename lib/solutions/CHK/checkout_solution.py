import json
from os import path


class Item:
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


root = 'C:\\Dev\\Python\\i3verticals\\accelerate_runner\\lib\\solutions\\CHK'


def load_table(file_path: str) -> dict:
    data = None
    abs_path = path.join(root, file_path)

    with open(abs_path, 'r') as file:
        data = json.load(file)

    return data


def load_item_prices() -> list:
    data = load_table('db\\items.json')
    items = []
    for d in data:
        p = Item(d["item_id"], int(d["price"]))
        items.append(p)

    return items


def load_discounts(cart) -> list:
    data = load_table('db\\discounts.json')
    discounts = []
    for d in data:
        p = Discount(d["discount_type"], d["item_list"], int(d["quantity"]),
                     int(d["amount"]), d["discounted_items"])

        # filter for only items in cart
        if len(list(filter(lambda c: c in p.item_list, cart))) > 0:
            discounts.append(p)

    # ensure we're handling the best discounts first
    sorted_discounts = sorted(
        discounts, key=lambda d: d.amount, reverse=True)
    return sorted_discounts


def get_eligible_discounts(discounts: list, item_id: str) -> list:
    eligible_discounts = []

    return filter(lambda d: item_id in d.item_list, discounts)


def process_basic_discount(discount: Discount, items: list, cart: dict) -> int:
    total = 0
    eligible_item = discount.item_list[0]
    item_to_discount = discount.discounted_items[0]

    item = next(
        filter(lambda i: i.item_id == eligible_item, items), None)

    discounted_item = next(filter(
        lambda i: i.item_id == item_to_discount, items), None)

    # eligible item should be the same as discounted item for basic discount
    if eligible_item in cart.keys() and item_to_discount == eligible_item:
        while cart[eligible_item] >= discount.quantity:
            # remove item from cart and add price - discount to total
            cart[eligible_item] -= discount.quantity

            # add the subtotal for the items less the discount to the final amount
            total += (item.price *
                      discount.quantity) - discount.amount

    return total


def process_bogo_discount(discount: Discount, items: list, cart: dict) -> int:
    total = 0
    eligible_item = discount.item_list[0]
    item_to_discount = discount.discounted_items[0]

    item = next(
        filter(lambda i: i.item_id == eligible_item, items), None)

    discounted_item = next(filter(
        lambda i: i.item_id == item_to_discount, items), None)

    if eligible_item in cart.keys():
        while cart[eligible_item] >= discount.quantity:
            # BOGO discount
            if item_to_discount in cart.keys() and cart[item_to_discount] > 0:
                cart[eligible_item] -= discount.quantity
                total += (item.price * discount.quantity)

                if cart[item_to_discount] > 0:
                    # could add this to discount object instead of hardcoding
                    cart[item_to_discount] -= 1
                    total += (discounted_item.price - discount.amount)
            else:
                break

    return total


def process_group_discount(discount: Discount, items: list, cart: dict) -> int:
    total = 0
    # sort discount items by price desc
    sorted_items = sorted(list(
        filter(lambda i: i.item_id in discount.item_list, items)), key=lambda d: d.price, reverse=True)

    cart_items = dict(
        filter(lambda c: c[0] in discount.item_list, cart.items()))

    item_count = 0
    # get exact number of items eligible for discount
    items_to_discount = sum(cart_items.values()) - \
        sum(cart_items.values()) % discount.quantity
    # 3

    # loop through until all eligible items are removed from cart

    for item in sorted_items:
        if items_to_discount == 0:
            break

        # subtract from cart item count until quantity is reached
        if item.item_id in cart_items.keys():
            # greater than discount.quantity # greater than or equal to
            while cart[item.item_id] >= discount.quantity:
                cart[item.item_id] -= discount.quantity
                total += discount.amount
                items_to_discount -= discount.quantity

            # item count less than remaining items_to_discount
            if cart[item.item_id] > 0 and items_to_discount > 0:
                items_to_discount -= cart[item.item_id]
                item_count += cart[item.item_id]
                cart[item.item_id] = 0

                if item_count >= discount.quantity:
                    total += discount.amount
                    item_count -= discount.quantity

    return total

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    cart = {}
    total = 0

    try:
        items = load_item_prices()

        # build the cart
        for s in skus:
            if s not in cart.keys():
                cart.setdefault(s, 0)
            cart[s] += 1

        discounts = load_discounts(cart.keys())

        for discount in discounts:
            if discount.discount_type == "basic":
                total += process_basic_discount(discount, items, cart)
            elif discount.discount_type == "BOGO":
                total += process_bogo_discount(discount, items, cart)
            elif discount.discount_type == "group":
                total += process_group_discount(discount, items, cart)

        # total remaining items after discounts
        for item_id in cart.keys():
            item = next(filter(lambda p: p.item_id == item_id, items), None)
            total += cart[item_id] * item.price

        return total
    except Exception as e:
        return -1


if __name__ == "__main__":
    print(checkout("ZZZ"))


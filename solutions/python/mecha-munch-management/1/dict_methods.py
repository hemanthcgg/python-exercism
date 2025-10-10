"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if(current_cart.get(item)):
            current_cart[item] = current_cart[item]+1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    return add_item({},notes)


def update_recipes(ideas, recipe_updates):
    ideas.update(dict(recipe_updates))
    return ideas


def sort_entries(cart):
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}
    item_names = list(cart.keys())
    item_names.sort(reverse=True)
    for item in item_names:
        quantity = cart[item]
        aisle_location, needs_refrigeration = aisle_mapping[item]
        fulfillment_cart[item] = [quantity, aisle_location, needs_refrigeration]
        
    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    for item, cart_details in fulfillment_cart.items():
        ordered_quantity = cart_details[0]
        if item in store_inventory:
            inventory_details = store_inventory[item]
            current_stock = inventory_details[0]
            if isinstance(current_stock, int):
                new_stock = current_stock - ordered_quantity
                if new_stock > 0:
                    inventory_details[0] = new_stock
                else:
                    inventory_details[0] = 'Out of Stock'
            store_inventory[item] = inventory_details
    return store_inventory

"""Functions to keep track and alter inventory."""


def create_inventory(items):
    result = {}
    for item in items:
        if(result.get(item)):
            result[item] = result[item]+1
        else:
            result[item] = 1
    return result


def add_items(inventory, items):
    for item in items:
        if(inventory.get(item)):
            inventory[item] = inventory[item]+1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if(inventory.get(item)):
            inventory[item] = inventory[item]-1
    return inventory


def remove_item(inventory, item):
    temp = inventory.pop(item,'')
    return inventory


def list_inventory(inventory):
    return [(key,value) for key,value in inventory.items() if(value>0)]


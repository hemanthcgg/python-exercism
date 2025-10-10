"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name,) + (set(dish_ingredients),)


def check_drinks(drink_name, drink_ingredients):
    if(set(drink_ingredients).isdisjoint(ALCOHOLS)):
        return drink_name + ' Mocktail'
    return drink_name + ' Cocktail'


def categorize_dish(dish_name, dish_ingredients):
    if(set(dish_ingredients).issubset(VEGAN)):
        return dish_name + ': VEGAN'
    if(set(dish_ingredients).issubset(VEGETARIAN)):
        return dish_name + ': VEGETARIAN'
    if(set(dish_ingredients).issubset(PALEO)):
        return dish_name + ': PALEO'
    if(set(dish_ingredients).issubset(KETO)):
        return dish_name + ': KETO'
    return dish_name + ': OMNIVORE'


def tag_special_ingredients(dish):
    dish_name, [*rest] = dish
    excess = SPECIAL_INGREDIENTS.intersection(rest)
    return (dish_name,)+(set(excess),)


def compile_ingredients(dishes):
    x, *rest = dishes
    for i in rest:
        x = x.union(i)
    return x


def separate_appetizers(dishes, appetizers):
    return list(set(dishes).difference(appetizers))


def singleton_ingredients(dishes, intersection):
    all_ingredients = set().union(*dishes)
    singleton_set = all_ingredients.difference(intersection)
    return singleton_set
        
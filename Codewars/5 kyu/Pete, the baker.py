def cakes(recipe, available):
    list = []
    for ing in recipe:
        if ing not in available:
            available[ing] = 0
    for ing in available:
        if ing not in recipe:
            recipe[ing] = 0
    for ing,ammount in available.items():
        try:
            list.append(ammount // recipe[ing])
        except ZeroDivisionError:
            continue

    return min(list)


recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))

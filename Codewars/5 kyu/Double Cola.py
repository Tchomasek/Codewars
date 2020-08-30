def who_is_next(names, r):
    for i in range(r):
        x=names.pop(0)
        names.append(x)
        names.append(x)
    return names[0]


names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
print(who_is_next(names, 7230702951))

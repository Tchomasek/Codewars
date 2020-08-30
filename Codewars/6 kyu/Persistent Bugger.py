"""Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
which is the number of times you must multiply the digits in num until you reach a single digit."""


def persistence(n):
    counter = 0
    while n > 9:
        counter+=1
        list = []
        n_str = str(n)
        for char in n_str:
            list.append(int(char))
        result = 1
        for i in list:
            result = result * i
        n=result
    return counter

print(persistence(39))

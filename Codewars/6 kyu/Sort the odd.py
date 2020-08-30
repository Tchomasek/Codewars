def sort_array(source_array):
    result = list(source_array)
    even = {}
    for index,num in enumerate(source_array):
        if num % 2 == 0:
            even[index] = num
            result.remove(num)
    result.sort()
    for index,num in even.items():
        result.insert(index, num)
    return result

print(sort_array([0, 1, 2, 3, 4, 9, 8, 7, 6, 5]))







"""You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]"""

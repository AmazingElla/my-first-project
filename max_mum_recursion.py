'''
Write two recursive functions:
1. find_max(numbers) – returns the largest number in a list.
2. find_min(numbers) – returns the smallest number in a list.
Requirements:
- Use recursion; no loops.
- Do not use max(), min() or sort().
- If the list is empty, raise a ValueError.
- If the input is not a list, raise a TypeError
'''

def find_max(numbers):
    if type(numbers) != list:
        raise TypeError("input must be a list")
    if numbers == []:
        raise ValueError("list must not be empty")
    if len(numbers) == 1:
        return numbers[0]
    rest_max = find_max(numbers[1:])
    if numbers[0] > rest_max:
        return numbers[0]
    else:
        return rest_max


def find_min(numbers):
    if type(numbers) != list:
        raise TypeError("input must be a list")
    if numbers == []:
        raise ValueError("list must not be empty")
    if len(numbers) == 1:
        return numbers[0]
    rest_min = find_min(numbers[1:])
    if numbers[0] < rest_min:
        return numbers[0]
    else:
        return rest_min

numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
print(find_max(numbers))
print(find_min(numbers))
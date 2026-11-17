'''
Write a recursive function called sum_of_natural_numbers(n) that calculates the sum of all natural numbers from 1 up to n.

Requirements:
1. The function must use recursion (no loops).
2. If n is 0, return 0.
3. If n is a negative number, raise a ValueError.
4. If n is not an integer, or if it is a Boolean, raise a TypeError.
5. Do not use Python's built-in sum() function.Here is a recursive function called `sum_of_natural_numbers(n)` that meets the specified requirements:

'''

def sum_of_natural_numbers(n):
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)

print(sum_of_natural_numbers(5))

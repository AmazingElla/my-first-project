numbers = [int(number)for number in input("Enter numbers separated by spaces: ").split()]

largest_num = None
smallest_num = None

for number in numbers:
    if largest_num is None:
        largest_num = number
    elif number > largest_num:
        largest_num = number

    if smallest_num is None:
        smallest_num = number
    elif number < smallest_num:
        smallest_num = number

print("Largest number is", largest_num)
print("Smallest number is", smallest_num)
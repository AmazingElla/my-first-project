numbers = [14, 3, 21, 8, 6, 19]

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

print("Largest number:", largest_num)
print("Smallest number:", smallest_num)

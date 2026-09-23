numbers = [8, 3, 12, 56, 90]

largest_num = None

for number in numbers:
    if largest_num is None:
        largest_num = number
    elif number > largest_num:
        largest_num = number

print("Largest number:", largest_num)

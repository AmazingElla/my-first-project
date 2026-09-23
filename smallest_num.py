numbers = [15, 4, 20, 7, 12]

smallest_num = None

for number in numbers:
    if smallest_num is None:
        smallest_num = number

    elif number < smallest_num:
        smallest_num = number

print("Smallest number:", smallest_num)
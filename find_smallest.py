numbers = [int(number)for number in input("Enter numbers separated by spaces: ").split()]

smallest_num = None

for number in numbers:
    if smallest_num is None:
        smallest_num = number

    elif number < smallest_num:
        smallest_num = number

print("Smallest number is", smallest_num)
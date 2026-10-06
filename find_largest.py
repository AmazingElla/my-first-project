numbers = [int(number)for number in input("Enter a list of numbers separated with comma: ").split(",")]

largest_number = None

for number in numbers:
    if largest_number is None:
        largest_number = number

    elif number > largest_number:
        largest_number = number
print("Largest number is", largest_number)
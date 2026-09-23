def find_largest_smallest(numbers):
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

numbers = [int(number)for number in input("Enter a list of numbers separated by commas: ").split()]
find_largest_smallest(numbers)

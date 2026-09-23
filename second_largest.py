def find_second_largest(numbers):
    largest_num = None
    second_largest = None

    for number in numbers:
        if largest_num is None:
            largest_num = number

        elif number > largest_num:
            second_largest = largest_num
            largest_num = number

        elif second_largest is None or number > second_largest:
            second_largest = number

    print("Largest number:", largest_num)
    print("Second largest number:", second_largest)

find_second_largest([3, 4, 5, 20, 10])
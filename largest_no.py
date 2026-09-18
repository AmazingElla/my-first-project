'''
we require 5 numbers, and from these numbers, we are going to determine which is the highest.
we need a variable to keep track of the largest number so far.
then, with that largest number variable, we will use it to compare with all the inputed numbers
know when you are to replace the current largest number,
if you identify the largest number, replace it and then print.

'''

for i in range(5):
    number = int(input("Enter number: "))

    if i == 0:
        largest = number

    elif number > largest:
        largest = number 
print(f"Largest number: {largest}")
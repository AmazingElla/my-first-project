#we want to check if a number that we will input, if it is positive, negative or zero.
#we want to see what will happen if the  number is a positive or negative.
def check_number(number):
    if number > 0:
        return("Positive.")

    elif number < 0:
        return("Negative")

    else:
        return("Zero")

number = int(input("Enter a number: "))
result = check_number(number)
print(result)
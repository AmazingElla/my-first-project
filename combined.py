number = int(input("Enter a number: "))

if number % 2 == 0 and number > 0:
    print("Positive and Even")

elif number % 2 != 0 and number > 0:
    print("Positive and Odd")

elif number < 0:
    print("Negative")

else:
    print("Zero")
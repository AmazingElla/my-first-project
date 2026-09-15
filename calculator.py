'''
enter the unit used. then calculate the unit of electricity used with the amount, and print the electricity bill
convert the input to an integer
then use the conditionals(if,elif,else) 
handle error cases - if the input is a negative number,
print Invalid number of units.
'''
no_of_units = int(input("Enter units used: "))

if no_of_units < 0:
    print("Invalid number of units")

else:
    if no_of_units > 100:
        electricity_bill = no_of_units * 50
        print(f"Electricity bill: ₦{electricity_bill}")

    elif no_of_units >= 51:
        electricity_bill = no_of_units * 30
        print(f"Electricity bill: ₦{electricity_bill}")

    else:
        electricity_bill = no_of_units * 20
        print(f"Electricity bill: ₦{electricity_bill}")
        

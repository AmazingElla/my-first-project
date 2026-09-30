'''
Practice Question: Movie Ticket Booking System

Write a Python program that determines whether a user can book a movie ticket and calculates the final ticket price.

Use the following information:

base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"
is_member = False
is_weekend = False

Your program should follow these rules:

A user must be older than 17 to be eligible to book a ticket.
A user must be at least 21 years old to attend an evening show.
A member who is at least 21 years old receives a $3 membership discount.
If the movie is playing on a weekend OR it is an evening show, add a $2 extra charge.
The ticket booking condition is satisfied if:
the user is at least 21, OR the user is at least 18 and either the show is not an evening show or the user is a member.
Apply service charges based on the seat type:
"Premium" → $5
"Gold" → $3
Any other seat type → $1
Calculate the final price using:
final_price = base_price + extra_charges + service_charges - discount
Print appropriate messages showing:
Whether the user is eligible to book.
Whether they qualify for the membership discount.
Whether extra charges apply.
The service charge.
The final ticket price.
Or, if they don't satisfy the booking conditions, print that the booking failed.
'''

base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"

if age > 17:
    print("You are eligible to book ticket.")

if age >= 21:
    print("You are eligible to attend evening show.")

else:
    print("You are not eligible to attend evening show.o ")

is_member = False
is_weekend = False

membership_discount = 0
extra_charges = 0

if is_member and age >= 21:
    membership_discount = 3
    print("User is qualified for the membership discount.")
else:
    print("User is not qualified for the membership discount.")

if is_weekend or show_time == "Evening":
    extra_charges = 2
    print("Extra charges will apply.")
else:
    print("Extra charges will not apply.")

if age >= 21 or age >= 18 and show_time != "Evening" or is_member:
    print("The ticket booking condition is satisfied.")

    service_charges = 0
    if seat_type == "Gold":
        service_charges = 3
    elif seat_type == "Premium":
        service_charges = 5
    else:
        service_charges = 1
    print("Service charges:", service_charges)
    final_price = (base_price + extra_charges + service_charges) - membership_discount
    print("Final price:", final_price)
else:
    print("The ticket booking failed.")
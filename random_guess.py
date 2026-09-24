import random

random_number = random.randint(1, 10)
attempt = 3
while attempt > 0:
    guess = int(input("Guess a number: "))
    if guess == random_number:
        print("You win.")
        break
    attempt -= 1
    if guess > random_number:
        print("Too high")
    else:
        print("Too low.")
    print("Guess again")
    if attempt == 0:
        print(f"You lose, the answer is {random_number}")
    
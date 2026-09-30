'''
create a calculator that takes a listas the history of previous totals, so that "undo"
can restore the previous state of the calculation.
we need the user to input the numbers
if the length of the input isn't 2, display invalid input.
'''

total = 0.0
history = []

while True:
    number = input("Enter operator and number, (e.g. + 5), or 'undo'/ 'quit': ")
    if number.lower() == "quit":
        break
    if number.lower() == "undo":
        if len(history) > 0:
            total = history.pop()
            print("Result:", total)
        else:
            print("Nothing to undo.")
            continue

    parts = number.split()
    if len(parts) != 2:
        print("Invalid input. Use an operator and a number, e.g. + 5")
        continue
    operator = parts[0]

    try:
        num = float(parts[1])
    except ValueError:
        print("Invalid number.")
        continue
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid Operator.")
        continue
    if operator == "/" and number == 0:
        print("Cannot be divided by zero")
        continue


    history.append(total)
    if operator == "+":
        total += num
    elif operator == "-":
        total -= num
    elif operator == "*":
        total *= num
    elif operator == "/":
        total /= num
    print("Result:", total)


'''
we want to determine whether or not the withdrawal can be successful and completed or not.
what is the first step? input of the account balance & the withdrawal amount
handle the error cases: if the withdrawal amount is greater than the balance, print "insufficient funds"
handle the second - if the withdrawal amount is 0 or less, print "invalid withdrawal amount"
else, complete the withdrawal and print the remaining balance.
'''
balance = int(input("Enter your balance: "))
withdrawal_amount = int(input("Enter withdrawal amount: "))

if withdrawal_amount > balance:
    print("Insufficient funds")

elif withdrawal_amount <= 0:
    print("Invalid withdrawal amount")

else:
    remaining_balance = balance - withdrawal_amount
    print("Withdrawal successful")
    print(f"Remaining balance: {remaining_balance} ")
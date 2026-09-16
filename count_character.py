'''
we will be counting how many times a character "a" appears in 
a word that is inputed. we will be using the input(), then create a variable that keeps track
of our count.then, we will create loop and assign it where it will go through,
use the if to check if there's an "a" character  in the word input
'''

word = input("Enter a word: ")

count = 0

for character in word:
    if character == "a":
        count += 1

print(f"The letter a appears {count} times")
'''
in this exercise, we are going to make use of indexing and len(). then, we will
also use loop cos we will be comparing characters from opposite ends. as we are comparing,
we will be needing a boolean, like is_palindrome, to check if it is true or not.
first step, to have the input.
'''

word = input("Enter a word: ")

is_palindrome = True

for i in range(0, len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        is_palindrome = False

if is_palindrome:
    print(f"{word} is a palindrome")

else: 
    print(f"{word} is a palindrome")
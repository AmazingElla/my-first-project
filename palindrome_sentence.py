'''
skip punctuation and spaces. Only consider numbers and alphabets - alphanumeric. we will use isalnum()
comapare the characters from left to right.
'''

sentence = input("Enter the sentence here: ")

left = 0
right = len(sentence) -1

is_palindrome = True

while left < right:
    if not sentence[left].isalnum():
        left += 1
        continue
    if not sentence[right].isalnum():
        right -= 1
        continue

    if sentence[left].lower() != sentence[right].lower():
        is_palindrome = False

    left += 1
    right -= 1
if is_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")

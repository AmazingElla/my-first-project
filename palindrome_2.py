word = input("Input: ")

is_palindrome = True

for i in range(0, len(word) // 2):
    if word[i] != word[- 1 - i]:
        is_palindrome = False

if is_palindrome:
    print(f"Input: {word} | Output: Palindrome")

else:
    print(f"Input: {word} | Output: Not a Palindrome")

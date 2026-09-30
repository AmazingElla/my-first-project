text = input("Enter a message: ")
shift = int(input("Enter the shift: "))
mode = input("Do you want to encrypt or decrypt? ")

result = ""

for char in text:
    if char.isalpha():
        if mode == "encrypt":
            new_position = (ord(char) - ord("a") + shift) % 26
        elif mode == "decrypt":
            new_position = (ord(char) - ord("a") - shift) % 26
        else:
            print("Invalid mode.")
            break
        new_character = chr(new_position + ord("a"))
        result += new_character

    else:
        result += char
print("Result:", result)
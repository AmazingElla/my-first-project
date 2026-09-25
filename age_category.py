age = int(input("Enter your age: "))

if age < 18:
    print("Minor")
elif 18 <= age <= 39:
    print("Young Adult")
else:
    print("Adult")
    
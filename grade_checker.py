'''
i am trying to get the input of each student name and score.
then, set conditions that will determine their grades.
'''

name = input("Enter student's name: ")
score = int(input("Enter score: "))

if score >= 70:
    grade = "A"
    print("Grade: A")

elif score >= 60:
    grade = "B"
    print('Grade: B')

elif score >= 50:
    grade = "C"
    print('Grade: C')

elif score >= 45:
    grade = "D"
    print('Grade: D')

elif score >= 40:
    grade = "E"
    print('Grade: E')

else:
    grade = "F"
    print('Grade: F')

print(f'Student: {name}, Grade: {grade}')
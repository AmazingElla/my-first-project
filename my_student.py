students = [
    {"name": "Ada", "scores": [80, 70, 90]},
    {"name": "John", "scores": [45, 50, 55]},
    {"name": "Mary", "scores": [90, 85, 95]},
    {"name": "Peter", "scores": [30, 40, 35]}
]

def calculate_average(scores):
    total = 0

    for score in scores:
        total += score
    return total / len(scores)

def grade_for(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"

def create_result(student):
    name = student["name"]
    average = calculate_average(student["scores"])
    grade = grade_for(average)
    return name, average, grade

results = list(map(create_result, students))

passed_students = list(filter(lambda result: result[2] in ("A", "B", "C"), results))

for name, average, grade in results:
    print(f"{name}: Average: {average:.2f} -> Grade: {grade}")

for name, average, grade in passed_students:
    print(f"{name}: Average: {average:.2f} -> Grade: {grade}")
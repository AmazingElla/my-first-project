# Employee Information and Code Extraction

This is a beginner-friendly Python program that demonstrates how to work with **strings, variables, string concatenation, type conversion, f-strings, and string slicing**.

## 📌 What This Program Does

The program:

* Stores an employee's first and last name.
* Combines the first and last name to create a full name.
* Creates and updates an address using string concatenation.
* Stores the employee's age and years of experience.
* Converts numbers to strings using `str()`.
* Creates an employee information card using an **f-string**.
* Extracts specific parts of an employee code using **string slicing**.

## 🐍 Concepts Used

### 1. Variables

The program stores information in variables such as:

```python
first_name = 'John'
last_name = 'Doe'
employee_age = 28
position = 'Data Analyst'
```

### 2. String Concatenation

The `+` operator is used to join strings together:

```python
full_name = first_name + ' ' + last_name
```

This produces:

```text
John Doe
```

The address is also updated using `+=`:

```python
address = '123 Main Street'
address += ', Apartment 4B'
```

### 3. Type Conversion

The employee's age and years of experience are numbers, so `str()` is used to convert them into strings before joining them with other text:

```python
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
```

### 4. F-Strings

An f-string is used to easily combine variables and text:

```python
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
```

### 5. String Slicing

The employee code is:

```text
DEV-2026-JD-001
```

Different sections are extracted using indexing and slicing:

```python
department = employee_code[0:3]
year_code = employee_code[4:8]
initials = employee_code[9:11]
last_three = employee_code[-3:]
```

This extracts:

* `DEV` → Department code
* `2026` → Year code
* `JD` → Employee initials
* `001` → Last three characters

## ▶️ How to Run

Make sure Python is installed on your computer.

Save the code in a Python file, for example:

```text
employee_info.py
```

Then run:

```bash
python employee_info.py
```

## 📤 Expected Output

```text
John Doe is 28 years old
Experience: 5 years
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
DEV
2026
JD
001
```

## 🎯 Learning Objective

This exercise is designed to practice basic Python concepts, especially:

* Variables
* Strings
* String concatenation
* `+=`
* Type conversion with `str()`
* F-strings
* String indexing
* String slicing
* Negative indexing
* Printing output with `print()`

## 📁 Project Structure

```text
employee-information/
│
├── employee_info.py
└── README.md
```

## 👩🏽‍💻 Author

Created as part of my Python learning journey.


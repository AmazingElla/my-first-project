# 🐍 Python Practice Exercises

This repository contains a collection of beginner-friendly Python exercises I completed while learning how to read, break down, and solve programming problems.

The goal of these exercises is not just to write code, but to understand the **thought process behind a Python program**:

> **Understand the problem → Identify the inputs → Convert the data → Apply conditions → Perform calculations → Handle errors → Display the output**

---

## 📚 Exercises

### 1. Student Grade Checker

**File:** `grade_checker.py`

#### Description

A program that accepts a student's name and score, validates the score, and determines the student's grade based on the grading system.

#### Grading System

| Score  | Grade |
| ------ | ----- |
| 70–100 | A     |
| 60–69  | B     |
| 50–59  | C     |
| 45–49  | D     |
| 40–44  | E     |
| 0–39   | F     |

Scores below `0` or above `100` are considered invalid.

#### Example

```text
Enter student's name: Alice
Enter score: 75

Student: Alice, Grade: A
```

#### Invalid Input Example

```text
Enter student's name: Alice
Enter score: 150

Invalid score
```

#### Concepts Practiced

* `input()`
* Type conversion using `int()`
* Variables
* Comparison operators
* `if / elif / else`
* Logical operators (`or`)
* Input validation
* Nested conditionals
* f-strings
* Assigning values to variables

---

### 2. Electricity Bill Calculator

**File:** `electricity_bill.py`

#### Description

A program that accepts the number of electricity units used and calculates the electricity bill based on the applicable rate.

#### Electricity Rates

| Units Used | Rate         |
| ---------- | ------------ |
| 0–50       | ₦20 per unit |
| 51–100     | ₦30 per unit |
| Above 100  | ₦50 per unit |

#### Example

```text
Enter units used: 40

Electricity bill: ₦800
```

Calculation:

```text
40 × ₦20 = ₦800
```

Another example:

```text
Enter units used: 120

Electricity bill: ₦6000
```

Calculation:

```text
120 × ₦50 = ₦6000
```

#### Invalid Input Example

```text
Enter units used: -5

Invalid number of units
```

#### Concepts Practiced

* `input()`
* Type conversion using `int()`
* Variables
* Arithmetic operators
* Comparison operators
* `if / elif / else`
* Input validation
* Conditional calculations
* f-strings
* Understanding how the order of conditions affects program execution

---

### 3. ATM Withdrawal

**File:** `atm_withdrawal.py`

#### Description

A simple ATM program that accepts a user's account balance and withdrawal amount, then determines whether the withdrawal can be completed.

#### Rules

* If the withdrawal amount is greater than the account balance → `Insufficient funds`
* If the withdrawal amount is `0` or negative → `Invalid withdrawal amount`
* Otherwise → Complete the withdrawal and display the remaining balance

#### Example

```text
Enter your balance: 50000
Enter withdrawal amount: 15000

Withdrawal successful
Remaining balance: 35000
```

#### Insufficient Funds Example

```text
Enter your balance: 10000
Enter withdrawal amount: 15000

Insufficient funds
```

#### Invalid Amount Example

```text
Enter your balance: 10000
Enter withdrawal amount: -500

Invalid withdrawal amount
```

#### Concepts Practiced

* `input()`
* Type conversion
* Variables
* Comparison operators
* `if / elif / else`
* Validation
* Arithmetic operations
* Conditional logic
* Producing different outputs based on different conditions

---

# 🧠 Problem-Solving Approach

For each exercise, I practiced breaking the question down before writing the code.

### Step 1 — Identify the inputs

Ask:

> What information does the program need from the user?

For example:

```text
Student Grade Checker:
→ Student name
→ Student score
```

### Step 2 — Identify the data types

Ask:

> What type of data should each input be?

For example:

```text
Name → string
Score → integer
```

Since `input()` returns a string by default, numerical input needs to be converted.

```python
score = int(input("Enter score: "))
```

### Step 3 — Identify the conditions

Ask:

> What decisions does the program need to make?

For example:

```text
Is the score below 0 or above 100?
Is the score 70 or above?
Is the score 60 or above?
...
```

These decisions can be represented using:

```python
if
elif
else
```

### Step 4 — Identify the calculation

Ask:

> What calculation needs to happen after the condition is met?

For example:

```python
electricity_bill = no_of_units * 50
```

### Step 5 — Handle invalid inputs

Ask:

> What happens if the user enters something that isn't allowed?

For example:

```python
if no_of_units < 0:
    print("Invalid number of units")
```

### Step 6 — Display the result

Finally, display the result using `print()`.

For example:

```python
print(f"Electricity bill: ₦{electricity_bill}")
```

---

# 🔑 Key Python Concepts Learned

Through these exercises, I practiced:

### Input and Type Conversion

```python
name = input("Enter your name: ")
score = int(input("Enter score: "))
```

### Variables

```python
score = 75
grade = "A"
```

### Comparison Operators

```python
>
<
>=
<=
==
```

### Logical Operators

```python
and
or
```

### Conditional Statements

```python
if
elif
else
```

### Arithmetic Operators

```python
+
-
*
/
```

### f-Strings

```python
print(f"Student: {name}, Grade: {grade}")
```

### Input Validation

Checking whether user input falls within the expected range before processing it.

---

#Repository Structure

```text
python-practice/
│
├── README.md
├── grade_checker.py
├── electricity_bill.py
└── atm_withdrawal.py
```

#Learning Goal

The main goal of these exercises is to become better at **processing programming questions independently**.

Rather than immediately writing code, I am learning to:

1. Understand what the question is asking.
2. Identify the required inputs.
3. Determine the appropriate data types.
4. Break the problem into smaller conditions.
5. Decide what calculations are required.
6. Handle invalid or unexpected inputs.
7. Translate the logic into Python.
8. Test the program with different inputs.
9. Debug errors and improve the solution.

These exercises are part of my journey toward becoming more confident and proficient in Python programming.

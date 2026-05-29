"""
Python Fundamentals to Real-World Problem Solving: Complete Beginner Guide
=========================================================================

This is a complete learning file containing THEORY + EXAMPLES.
Everything is written as comments so you can read it while learning Python.
"""

# --------------------------------------------------------------
# 1. PYTHON IDENTIFIERS (THEORY)
# --------------------------------------------------------------
# Identifiers are names used for variables, functions, classes, etc.

# Rules:
# - Can contain letters, digits, underscores
# - Cannot start with a digit
# - Cannot use Python keywords
# - Case-sensitive

username = "John"
age_1 = 25

# Invalid example:
# 1name = "Alex"


# --------------------------------------------------------------
# 2. NAMING CONVENTIONS (THEORY)
# --------------------------------------------------------------
# Variables → lowercase_with_underscores
# Constants → UPPERCASE
# Functions → descriptive names

student_name = "Rahul"
PI = 3.14159

def calculate_total():
    pass


# --------------------------------------------------------------
# 3. OPERATORS (THEORY)
# --------------------------------------------------------------
# Arithmetic: + - * / % **
# Comparison: == != > < >= <=
# Logical: and, or, not


# --------------------------------------------------------------
# 3.1 ARITHMETIC OPERATORS
# --------------------------------------------------------------
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

# Real-world example:
price = 1000
discount = 200
final_price = price - discount
print(final_price)


# --------------------------------------------------------------
# 3.2 COMPARISON OPERATORS
# --------------------------------------------------------------
age = 18
print(age >= 18)


# --------------------------------------------------------------
# 3.3 LOGICAL OPERATORS
# --------------------------------------------------------------
username = "admin"
password = "1234"

print(username == "admin" and password == "1234")


# --------------------------------------------------------------
# 4. STRINGS (THEORY)
# --------------------------------------------------------------
message = "Hello Python"

# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# Repetition
print("Python " * 3)

# Indexing
text = "Python"
print(text[0])
print(text[-1])

# Methods
name = "python"
print(name.upper())
print(name.lower())
print("  hello  ".strip())
print("I like Java".replace("Java", "Python"))
print("a,b,c".split(","))

# Real-world
name = input("Enter your name: ")
print("Welcome", name)

email = "user@gmail.com"
print("@" in email)

product = "Laptop"
price = 50000
print(f"Price of {product} is {price}")


# --------------------------------------------------------------
# 5. DATA STRUCTURES (THEORY)
# --------------------------------------------------------------

# LIST
fruits = ["apple", "banana", "mango"]

# TUPLE
coordinates = (10, 20)

# SET
numbers = {1, 2, 3, 3}

# DICTIONARY
student = {
    "name": "Rahul",
    "age": 21
}


# --------------------------------------------------------------
# 6. COMMON MISTAKES (THEORY)
# --------------------------------------------------------------

# Bad naming
employee_salary = 50000

# Indentation
if True:
    print("Hello")

# Tuple immutability
data = (1, 2, 3)

# Comparison operator
x = 5
if x == 5:
    print("Correct")


# Infinite loop (DO NOT RUN UNLESS NEEDED)
# while True:
#     print("Running")


# --------------------------------------------------------------
# 7. REAL-WORLD EXAMPLES
# --------------------------------------------------------------

# Student system
students = {"Rahul": 85, "Anita": 92}

for name, marks in students.items():
    print(name, marks)

# Shopping cart total
prices = [100, 250, 300]
total = 0

for price in prices:
    total += price

print(total)

# Remove duplicates
items = ["apple", "banana", "apple"]
print(set(items))

# Login system
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")


# --------------------------------------------------------------
# 8. CONCLUSION
# --------------------------------------------------------------
# Practice Python daily.
# Build small projects.
# Learn step by step.
# Become consistent.
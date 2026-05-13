# Day 1 - Python Basics

# Variables
name = "Vishnupriya"
age = 21

print("Name:", name)
print("Age:", age)

# Datatypes
print(type(10))
print(type(2.5))
print(type("Hello"))
print(type(True))

# Operators
print("Addition:", 2 + 4)
print("Subtraction:", 10 - 5)
print("Multiplication:", 3 * 4)
print("Division:", 10 / 2)
print("Power:", 2 ** 3)
print("Remainder:", 5 % 2)

# Math Functions
print("Round Value:", round(3.1))
print("Absolute Value:", abs(-20))

# Input Output
user_name = input("Enter your name: ")

print("Hello", user_name)

# Simple If Else
number = 10

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Loop
for i in range(1, 6):
    print(i)
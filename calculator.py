# Write a program that takes two numbers and an operator (+, -, *, /) as input and prints the result.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input('Enter operator: ')

calculator = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply
}

results = calculator[operator](num1, num2)

print(f'{num1} {operator} {num2} = {results}')


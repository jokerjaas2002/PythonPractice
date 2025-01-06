def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

def calculator():
   while True:
       print('Options:')
       print('Enter "add" for addition')
       print('Enter "subtract" for subtraction')
       print('Enter "multiply" for multiplication')
       print('Enter "divide" for division')
       print('Enter "quit" to end the program')
       user_input = input(': ')

       if user_input == 'quit':
           break
       elif user_input == 'add':
           num1 = float(input('Enter first number: '))
           num2 = float(input('Enter second number: '))
           print('Result:', add(num1, num2))
       elif user_input == 'subtract':
           num1 = float(input('Enter first number: '))
           num2 = float(input('Enter second number: '))
           print('Result:', subtract(num1, num2))
       elif user_input == 'multiply':
           num1 = float(input('Enter first number: '))
           num2 = float(input('Enter second number: '))
           print('Result:', multiply(num1, num2))
       elif user_input == 'divide':
           num1 = float(input('Enter first number: '))
           num2 = float(input('Enter second number: '))
           print('Result:', divide(num1, num2))
       else:
           print('Invalid input')


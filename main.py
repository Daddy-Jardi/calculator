def add():
    num1 = float(input('What is the first number? '))
    num2 = float(input('What is the second number? '))
    sum = num1 + num2
    print(f'The sum of {num1} and {num2} is equal to {sum}')

def subtract():
    num1 = float(input('What is the first number? '))
    num2 = float(input('What is the second number? '))
    answer = num1 - num2
    print(f'The difference of {num1} and {num2} is equal to {answer}')

operation = input('What math operation would you like to do? ')

if operation == 'add':
    add()
elif operation == 'subtract':
    subtract()





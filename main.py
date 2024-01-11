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

def multiply():
    num1 = float(input('What is the first number? '))
    num2 = float(input('What is the second number? '))
    answer = num1 * num2
    print(f'The multiplication of {num1} and {num2} is equal to {answer}')

def operation():
    question = input('What math operation would you like to do? ').lower()
    if question == 'add':
        add()
    elif question == 'subtract':
        subtract()
    elif question == 'multiply':
        multiply()
    else:
        print('Not an operation I can perform!')
        operation()

operation()



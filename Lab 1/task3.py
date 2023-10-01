import os

while True:
    os.system('cls')

    num1 = int(input('num1: '))
    num2 = int(input('num2: '))
    action = input('action(+, -, /, *): ')

    if action == '+':
        print(f'num1 + num2 = {num1 + num2}')
    elif action == '-':
        print(f'num1 - num2 = {num1 - num2}')
    elif action == '/':
        print(f'num1 - num2 = {num1 / num2}')
    elif action == '*':
        print(f'num1 - num2 = {num1 * num2}')
    else:
        print('incorrect action !!')

    os.system('pause')

print("This is simple calculator. Enter x and y, then enter operation")

x = int(input('Input x = '))
y = int(input('Input y = '))
sign = input('Input sign: ')

if sign == '+': print('Sum = ', x + y)

elif sign == '-': print('Dif = ', x - y)

elif sign == '*': print('Op = ', x * y)

elif sign == '/':
    while y == 0:
        print('Zero division error!')
        y = int(input('Input y = '))
        continue
    else:
        print('Div = ', x / y)
input('Press any key to continue')
"""
    restart = input('Do you want to continue y/n?')
    if restart == 'y':
        calc()
    elif restart == 'n':
        print('Bye')
    else:
        print('I guess it means stop. Bye')"""

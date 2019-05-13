print("This is simple calculator. Enter x and y, then enter operation")
cicle = 1
while cicle == 1:

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

#           New iteration of cicle

    c = input("Wanna input some more stuff? y/n")
    if c == 'y' or c == 'Y':
         print('Lets try in again')
    elif c == 'n' or c == 'N':
        print('Ok, bye mate')
        cicle = 0
input('Press any key to continue')

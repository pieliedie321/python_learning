print("This is simple calculator. \nEnter x and y, then enter operation sign.")
h = "Signs: Sum - '+', Difference - '-', Multiplication - '*', Division - '/'\nHere some few new signs: Exponentiation in degree - '**', Root - 'root'"
print(h)
print("Few words about 'root'. It works like this:\n'Degree's root y from number x'")

#   Adding calculate functions

def sum(x, y):
    z = float(x) + float(y)
    return z

def dif(x, y):
    z = float(x) - float(y)
    print('Difference is ', z)

def mult(x, y):
    z = float(x) * float(y)
    print('Multiplication is ', z)

def div(x, y):
    z = float(x) / float(y)
    print('Division is ', z)

def root(x, y):
    z = pow(float(x), 1/float(y))
    print("The degree's root y from x is", z)

def expon(x, y):
    z = pow(float(x), float(y))
    print('Exponentiation in degree is ', z)

#   Adding cicles in calculator

main_cicle = 1
x_cicle = 1
y_cicle = 1
sign_cicle = 1

#   Adding tuple for signs check

signs_tuple = ('+', '-', '*', '/', '**', 'root')

#   Starting calculator

while main_cicle == 1:

#   Cicles for numbers and sign input

    while x_cicle == 1:
        x = input('Input x:\n')
        try:
            type(int(x)) is int or type(float(x)) is float
            x_cicle = 0
        except ValueError:
            print('This is not a number. Try to input x again')

    while y_cicle == 1:
        y = input('Input y:\n')
        try:
            type(int(y)) is int or type(float(y)) is float
            y_cicle = 0
        except ValueError:
            print('This is not a number. Try to input y again')

    while sign_cicle == 1:
        sign = input('Input sign:\n')
        if sign not in signs_tuple:
            print('Try to input right sign. Here is some help info for you:')
            print(h)
            continue
        elif sign == '/' and y == 0:
            print("You can't divide by zero\n Try to input another sign")
        else:
            sign_cicle = 0

    if sign == '+':
        print('Sum is ', sum(x, y))

    elif sign == '-':
        dif(x, y)

    elif sign == '*':
        mult(x, y)

    elif sign == '/':
        div(x, y)

    elif sign == "**":
        expon(x, y)

    elif sign == 'root':
        root(x, y)

#   End cicle calculate repeat

    end_cicle = 1
    while end_cicle == 1:
        c = input("Do ypu want to input some more numbers?\ny/n\n")
        if c == 'y' or c == 'Y':
            print('Alright. Lets try in again')
            end_cicle = 0
        elif c == 'n' or c == 'N':
            print('Goodbye')
            end_cicle = 0
            main_cicle = 0
        else:
            print('Wrong answer, try one more time.\nYou want to input some more stuff?\ny/n ')
            continue

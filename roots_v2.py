import math
print('This is the simple calculator for equations like ax^2 + bx + c = 0. You need to imput a, b and c')
cicle = 1
while cicle == 1:
    a = float(input('Input a = '))
    b = float(input('Input b = '))
    c = float(input('Input c = '))
    D = b*b - 4*a*c
    if D > 0:
        print('D = ', D, '. D > 0, 2 roots')
        D_up1 = -b + math.sqrt(D)
        D_up2 = -b - math.sqrt(D)
        D_down = 2*a
        x1 = float(D_up1 / D_down)
        x2 = float(D_up2 / D_down)
        print('Roots: ', x1, 'and ', x2)
    elif D == 0:
        print('D = 0, 1 root')
        x = -b / 2*a
        print('Root: ', x)
    elif D < 0:
        print('D = 0, no roots')
    cont = input('Got another equation? (y/n)')
    if cont == 'y' or cont == 'Y':
        print('Alright, type another one')
    elif cont == 'n' or cont == 'N':
        cicle = 0
        print('See ya')
    else:
        print("Unknown command. Back to equation's question (y/n)")
        continue
input()

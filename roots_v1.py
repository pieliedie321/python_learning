import math
cic = True
while cic = True:
    a = float(input('Input a = '))
    b = float(input('Input b = '))
    c = float(input('Input c = '))
    D = b*b - 4*a*c
    if D > 0:
        print('D = ', D, '. D > 0, 2 roots')
        D_up1 = -b + math.sqrt(D)
        D_up2 = -b - math.sqrt(D)
        D_down = 2*a
        print(D_up1, D_up2, D_down)
        x1 = float(D_up1 / D_down)
        x2 = float(D_up2 / D_down)
        print('Roots: ', float(x1), 'and ', float(x2))
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
        print('See ya')
        cic = False
    else:
        print("Unknown command. Back to equation's question (y/n)")
        continue
input()

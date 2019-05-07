import math
a = float(input('Input a = '))
b = float(input('Input b = '))
c = float(input('Input c = '))
D = b*b - 4*a*c
if D > 0:
    print('D = ', D, '. D > 0, 2 roots')
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    print('Roots: ', x1, 'and ', x2)
elif D == 0:
    print('D = 0, 1 root')
    x = -b / 2*a
    print('Root: ', x)
elif D < 0:
    print('D = 0, no roots')
input()


cicle = 1
while cicle == 1:
    a = input('a = ')
    b = input('b = ')
    print(int(a) + int(b))
    print('do again? (y/n)')
    x = input()
    if x == 'y':
        cicle = 1
    elif x == 'n':
        cicle = 0
        print('bye')
input()

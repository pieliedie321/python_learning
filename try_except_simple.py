cicle = 1
while cicle == 1:
    x = input('Input x = ')
    try:
        type(int(x)) is int or type(float(x)) is float
        cicle = 0
    except ValueError:
        print('This is not a number. Try to input x again')
    

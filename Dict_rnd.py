import random
a = int(input('inner border = '))
b = int(input('external border = '))
x = random.randint(a, b)
D = {x: random.randint(a, b) for x in range(random.randint(a, b))}
sorted(D)
print(D)

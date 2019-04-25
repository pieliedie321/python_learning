L = []
X = 5
p = 2**X    #   2**X now out of cicle

for x in range(7):
    L.append(2**x)
    print(L)

if p in L:
    print(2**X, ' found at index ', L.index(p))
else:
    print(X, ' not found')

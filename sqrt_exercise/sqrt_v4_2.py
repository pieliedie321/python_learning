L = list(map(lambda x: 2 ** x, range(7)))   #   List with map func
print(L)
X = 5
p = 2**X    #   2**X now out of cicle

if p in L:
    print(2**X, ' found at index ', L.index(p))
else:
    print(X, ' not found')

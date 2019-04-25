L = [1, 2, 4, 8, 16, 32, 64]
X = 5
p = 2**X
if p in L:
    print(2**X, ' found at index ', L.index(p))
else:
    print(X, ' not found')

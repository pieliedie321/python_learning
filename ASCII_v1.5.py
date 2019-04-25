# First version released!
# In second version, i'm adding new feature: Sum of all simbols in S
print('Input the word and see whats happend')
S = input('Input word ')
L = []

for x in list(S):
    print('ASCII of ', x, ' => ', ord(x))
    L.append(int(ord(x)))

print('List of all codes are - ', L)

a = sum(L)
print('Sum = ', a)

input('Press any key to continue')

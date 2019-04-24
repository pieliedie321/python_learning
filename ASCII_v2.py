# First version released!
# In second version, i'm adding new feature: Sum of all simbols in S
print('Input the word and see whats happend')
c = 0
L = []
S = input('Input word ')
for x in list(S):
    print('ASCII of ', x, ' = ', ord(x))
    print('Now see sum of all ASCII codes!')
    c += ord(x)
    print('Summ = ', c)
    print('List of all codes are - ', L.append(ord(x)))
input('Press any key to continue')

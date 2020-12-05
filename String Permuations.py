

from itertools import permutations

s1=input("Enter string: ")

s2 = permutations(s1)

for i in list(s2):
    print(''.join(i))



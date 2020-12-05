
s1 = input("Enter string1: ")

print(s1)

l = len(s1)

cs = [False]*128

res = 1

for i in range(0, l):

    v = ord(s1[i])
    if cs[v]:
        res = 0
    else:
        cs[v] = True

if res!=1:
    print("Not unique")
else:
    print("Unique")

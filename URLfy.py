
s1 = input("Enter string: ")

list = []

for i in range(len(s1)):

    if(s1[i]==' '):
        list.extend('%')

    else:
        list.extend(s1[i])

s = ''

for i in list:
    s=s+i

print(s)
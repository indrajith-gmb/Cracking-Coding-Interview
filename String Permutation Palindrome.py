

char_array = 256

def permOrNot(str):

    count = [0] * (char_array)

    for i in range(0, len(str)):

        count[ord(str[i])] = count[ord(str[i])] + 1


    odd = 0

    for i in range(0, char_array):
        if(count[i]!=0):
            print(count[i])
        if(count[i] & 1):
            odd = odd + 1

        if(odd > 1):
            return False
    return True

s = input(("Enter string : "))

if(permOrNot(s)):
    print("Can form Palindrome")

else:
    print("Not forms Palindrome")
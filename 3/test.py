'''
#Reverse a string


def rev(s):
    if len(s) == 1:
        return s
    else:
        return rev(s[1:	]) + s[0]

print rev('2356')

'''


# Palindrome

def Palindrome(s):

    stack = []
    for i in s:
        stack.append(i)

    print stack

    list = []
    for i in range(len(stack)):
        list.append(stack.pop())
    print list

    for x,y in zip(stack, list):
        print x, y

print Palindrome("921")

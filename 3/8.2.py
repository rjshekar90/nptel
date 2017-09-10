
# Sum of the list of Numbers

def sumLists(l):
    if l == []:
        return 0

    else:
        return l[0] + sumLists(l[1:])

print sumLists([3,9,10])

#Length of a list recursively

def length(l):
    if l == []:
        return 0
    else:
        return 1 + length(l[1:])

print length([1,2,3])

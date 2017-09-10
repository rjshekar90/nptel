
def findpos(l, v):
    pos = -1
    for i in range(len(l)):
        if l[i] == v:
            pos = i
    return pos

print findpos([1,2,3], 3)

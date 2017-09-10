# Search for a value in a list

#Sequential search

def findPos(l, v):

    pos = -1

    for i in range(len(l)):
        if l[i] == v:
            pos = i
            break

    return pos

print findPos([100, 20, 30, 40], 40)

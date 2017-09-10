# Find a value in a list
# for and while loop can have a else clause

def findPos(l, v):

    #pos = 0        #Not Needed here
    for i in range(len(l)):
        if l[i] == v:
            pos = i         #can declare here
            break

    else:       # When the upper loop terminates normally, this else clause is executed.
        pos = -1

    return pos

print findPos([100, 20, 30, 40], 20)


#Linked List
#Insert, Delete, append

class Node:
    def __init__(self, initval = None):
        self.value = initval
        self.next = None

    def isEmpty(self):
        return (self.value == None)

    '''def append(self, v):
        if self.isEmpty():
            self.value = v
        elif self.next == None:
            newNode = Node(v)
            self.next = newNode
        else:
            self.next.append(v)         #Recursive call

        return ()   '''

    def appendi(self, v):       #Iterative approach
        if self.isEmpty():
            self.value = v
            return

        temp = self
        while temp.next != None:
            temp = temp.next
        newNode = Node(v)
        temp.next = newNode

        return

    #Insert a value at front.
    #We have to swap the value to avoid disconnection

    def insert(self, v):
        if self.isEmpty():
            self.value = v
            return
        newNode = Node(v)

        (self.value, newNode.value) = (newNode.value, self.value)
        (self.next, newNode.next) = (newNode, self.next)

        return

    #delete a Node x
    def delete(self, x):
        if self.isEmpty():
            return
        if self.value == x:      #delete if its first Node

            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return

        #delete if node is in middle or last:
        #See slides for recursive delete
        temp = self
        while temp.next != None:
            if temp.next.value == x:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next

        return

    def __str__(self):
        selflist = []
        if self.value == None:
            return (str(selflist))

        temp = self
        selflist.append(temp.value)

        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))








#Create a empty List

l = Node()
for i in range(1, 13):
    l.appendi(i)

print l

l.delete(10)
print l
l.insert(100)
print l

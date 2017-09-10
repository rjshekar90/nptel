#Binary Search Tree
#o(log n) --- balanced trees for n nodes

class Tree:

    def __init__(self, initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()      #if tree has left and right values
            self.right = Tree()
        else:
            self.left = None        #if tree has no child
            self.right = None
        return

    #Empty node has value None
    def isEmpty(self):
        return(self.value == None)
    #leaf nodes have both children Empty
    def isleaf(self):
        return(self.left.isEmpty() and self.right.isEmpty())

    #inorder trav.
    #output is always sorted.
    #use this to check if tree is sorted.
    def inorder(self):
        if self.isEmpty():
            return []
        else:
            return(self.left.inorder() + [self.value] + self.right.inorder())

    def __str__(self):
        return(str(self.inorder()))

    #find the value

    def find(self, v):
        if self.isEmpty():
            return False

        if self.value == v:
            return True

        if v < self.value:
            return self.left.find(v)
        else:
            return self.right.find(v)

    #Find the min value

    def minval(self):
        # assume t is not empty
        if self.left == None:
            return self.value
        else:
            return self.left.minval()

    #max value

    def maxval(self):
        # t is not empty
        if self.right == None:
            return self.value
        else:
            return self.right.maxval()

    #Insert v

    def insert(self, v):
        if self.isEmpty():      #add v as new leaf
            self.value = v
            self.left = Tree()
            self.right = Tree()

        if self.value == v:     #value found, do nothing
            return

        if v < self.value:
            self.left.insert(v)
            return

        if v > self.value:
            self.right.insert(v)
            return

    def delete(self, v):
        if self.isEmpty():
            return
        if v < self.value:
            self.left.delete(v)
            return
        if v > self.value:
            self.right.delete(v)
            return

        if v == self.value:
            if self.isleaf():
                self.makeempty()
            elif self.left.isEmpty():
                self.copyright()


            else:
                self.value = self.left.maxval()
                self.left.delete(self.left.maxval())
            return

    def makeempty(self):
        self.value  = None
        self.left = None
        self.right = None
        return

    def copyright(self):
        self.value = self.right.value
        self.left = self.right.left
        self.right = self.right.right
        return


t = Tree()

for i in [1, 5, 3, 6, 9, 99, 67, 54, 94]:
    t.insert(i)

print t

t.delete(9)

print t

t.insert(7)

print t

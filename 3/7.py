# https://www.youtube.com/watch?v=QnjToZfpi0E&feature=youtu.be
#Insertion Sort without building a new sequence
#O(n2)

def InsertionSort(l):

    for sliceEnd in range(len(l)):
        #build longer and longer sorted slices
        #In each iteration 0:sliceEnd already sorted

        #Move first element after sorted slice left
        #till it is in correct place.
        
        pos = sliceEnd

        while pos > 0 and l[pos] < l[pos - 1]:
            (l[pos], l[pos - 1]) = (l[pos - 1], l[pos])
            pos = pos - 1
    return l

print InsertionSort([74, 32, 89, 55, 25, 64])

#https://www.youtube.com/watch?v=zjqzrcljMlI&feature=youtu.be&t=594

# QuickSort
# Uses green and yellow pointers.
# yellow stays at values smaller than pivot. Green moves
# for values larger than pivot
#Pivot is usually the first value.


def quickSort(A, l, r):     #Sort A[l:r]
    if (r - l) <= 1:
        return

    #partition wrt pivot, a[l]
    yellow = l+1

    for green in range(l+1, r):
        if A[green] <= A[l]:            #A[l] is the pivot here
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow = yellow + 1

    #Move pivot into place

    (A[l], A[yellow - 1]) = (A[yellow - 1], A[l])

    quickSort(A, l, yellow-1)       #Recursive calls
    quickSort(A, yellow, r)

    return A

A = [3,4,5,7,1,2,9]
print quickSort(A, 0, len(A))

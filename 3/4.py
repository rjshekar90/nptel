# Binary Search
# Possible in Arrays only
# O(log(n))
# Use shft+ctrl+b
from __future__ import division

def binSearch(seq, v, l, r):

    if (r - l) == 0:        #If no slicing occurs at the end
        return "False"

    mid = (l + r)//2         #Uses Floor division

    if v == seq[mid]:
        return "True"

    if v < seq[mid]:
        return binSearch(seq, v, l, mid)

    else:
        return binSearch(seq, v, mid+1, r)

s = [1,2,3,4,5]

print binSearch(s, 0, 0, len(s))

#Selection Sort
#Uses 2 for loops. First one scans and stops
#second one scans thhrough the end.

def SelectionSort(l):

    for start in range(len(l)):     #start the first loop
        minpos = start              #set minpos as start i, 0, 1 ....

        for i in range(start, len(l)):  #start the second loop
            if l[i] < l[minpos]:        #compare the list values.
                minpos = i
        (l[start], l[minpos]) = (l[minpos], l[start])   #swap the list values

    return l

print SelectionSort([74, 32, 89, 55, 21, 64])

#GCD
#Euclids algo
#Best way to solve GCD. Very Few steps taken with this algo.
#refer nptel

def gcd(m, n):

    if m < n:  #Assume m >= n
        (m, n) = (n, m)

    while m%n != 0:
        (m, n) = (n , m%n) #m%n is remainder

    return n


print gcd(100, 30)

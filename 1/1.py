
# GCD

def gcd(m, n):

    fm = []
    for i in range(1, m+1):
        if m%i == 0:
            fm.append(i)

    fn = []
    for j in range(1, n+1):
        if n%j == 0:
            fn.append(j)

    cn = []
    for x in fm:
        if x in fn:
            cn.append(x)

    return cn[-1]

print gcd(8, 12)

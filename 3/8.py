
#Inductive definitions give rise to recursive computations

def multiply(m, n):
    if n == 1:
        return m
    else:
        return (m + multiply(m, n - 1))

print multiply(8, 8)

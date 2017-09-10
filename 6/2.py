
#Prints the value 7
#immutable if inside
def f():
    y = x
    print y
    x = 22      # gives an error, if x is def in f() and outside also

x = 7

f()

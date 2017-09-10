
#mutable values
'''  def f():
    y = x[0]
    print y
    x[0] = 22      #here x takes the value 7 instead of 22.

x = [7]
f()
'''

#global to update immutable values

def f():
    global x    #converts the 22 to global value.
    y = x       #refers to the outside one.
    print y
    x = 22

x = 7
f()
print x

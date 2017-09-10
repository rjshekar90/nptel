def f(*args, **kwargs):
    print ("Arguments", args)
    print ("keyword args", kwargs)

f(3,4,9, foo = 32, hello = 23)

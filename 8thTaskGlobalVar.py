x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def mynewfunc():
    x = "fantastic"
    print("Python is " + x)

mynewfunc()

print("Python is " + x)

def mynewestfunc():
    global x
    x = "fantastic!"
    print("Python is " + x)
mynewestfunc()

print("Python is " + x)

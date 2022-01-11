y=100 #global variable
def outer():
 # local variable
 # printing global   variable
    def inner():
        global y
        y=y*12
        print(y) # enclosed variable
    inner()

outer()
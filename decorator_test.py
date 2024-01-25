def decor_1(func2):
    def outer_1(*args, **kwargs):
        print ("inside outer_1 func......")
        x = func2(*args, **kwargs)
        print ("func2", x)
        print ("finished")
        return x * 30
    return outer_1

def decor(func1):
    def outer(*args, **kwargs):
        print ("inside outer func......")
        x = func1(*args, **kwargs)
        print ("func1", x)
        return x * 30
    return outer

def decor1(func):
    print ("inside @decor1......")
    def inner(*args, **kwargs):
        print ("*args:", *args)
        print ("*kwargs", *kwargs)
        print ("Inside inner function......")
        x = func(*args, **kwargs)
        print ("func:" ,x)
        print ("after excution")
        return x * 20    
    return inner

#adding decor_1 to the decor:
@decor_1
#adding decor to the decor1:
@decor
#adding decor1 to this function:
@decor1
def sum(a, b):
    print ("inside the sum func......")
    return a + b        

a,b = 3, 4

print ("result is :", sum(a, b))
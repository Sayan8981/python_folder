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

# Factorial program with memoization using
# decorators.
 
# A decorator function for function 'f' passed
# as parameter
memory = {}
def memoize_factorial(f):
     
    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]
 
    return inner
     
@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)
 
print(facto(5))
print(facto(5)) # directly coming from saved memory



def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function ran")

display()

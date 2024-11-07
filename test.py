def hello_decorator1(func1):
    def inner2():
        print ("another decorator called........")
        func1()
    return inner2   

# defining a decorator  
def hello_decorator(func):  
    
    # inner1 is a Wrapper function in   
    # which the argument is called  
        
    # inner function can access the outer local  
    # functions like in this case "func"  
    def inner1():  
        print("Hello, this is before function execution")  
    
        # calling the actual function now  
        # inside the wrapper function.  
        func()  
    
        print("This is after function execution")  
            
    return inner1  

@hello_decorator1    
@hello_decorator    
# defining a function, to be called inside wrapper  
def function_to_be_used():  
    print("This is inside the function !!")  
    
    
# passing 'function_to_be_used' inside the  
# decorator to control its behavior 
 
#function_to_be_used = hello_decorator(function_to_be_used)  
    
    
# calling the function  
function_to_be_used()

lst = [1, 2, 3, 4]
dict_ = {"a":1, "b":2, "c":3, "d":4}

sqr_list = [num**2 for num in lst]
print("This is the squre list:", sqr_list)
print (dict_.items())
dict_list = {num[0]:num[1]**3 for num in dict_.items()}
print (dict_list)
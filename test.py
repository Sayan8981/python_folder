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




# print the list in sorted descending order

list_ = [11,3,66,77,43,90] #op : [90,77,66,43,11,3]

temp = []

for i in range(len(list_)):
    for j in range(0, len(list_) - i - 1):
        if list_[j] < list_[j + 1]:  # Swap if the element found is smaller than the next element
            list_[j], list_[j + 1] = list_[j + 1], list_[j]           
            
print (list_)

#reverse of a string

strng = "Saayan Das"
temp = []
print (strng)

#import pdb;pdb.set_trace()

for i in range(0,len(strng)):
    temp.append(strng[len(strng)-i-1])
            
    
print ("".join(temp))
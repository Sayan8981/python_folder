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


#to get the maximum sum of the two adjascent letters
data = {"a": 16, "b": 12, "c":13, "d":25, "e":40}

temp = []

for item in data.values():
    temp.append(item)
   
print (temp)
sum_ = [0]
letters = [0] 

for i in range(len(temp)):
    for j in range (0, len(temp)):
        if j != i and temp[i]+temp[j] > sum_[0]: 
           sum_[0] = temp[i] + temp[j]
           
print (sum_) 
           
                        

lst = [1,2,3,4,5,6]


def func(lst):
    temp = []
    print (lst)
    for index in range(len(lst)-1, 0, -1):  
        #import pdb;pdb.set_trace()      
        temp.append(lst[index])
    print (temp)
    temp.insert(0, lst[0])
    #import pdb;pdb.set_trace()
    return temp

print (func(lst))     


a = lambda x,y : x * y 


class test(object):

    def __init__(self):

        self.employee_name = 'Saayan Das'
        self.employee_adress = "XYZ"

    def func1(self, employee_name, employee_adres):
        self.employee_name = employee_name
        self.employee_adress = employee_adres
        return (self.employee_name, self.employee_adress)

    def func(self):
        return (self.employee_name, self.employee_adress)

 
obj_ = test()

chnge = obj_.func1("saayanDas", "rytu")

print (chnge)

print (obj_.func())


           
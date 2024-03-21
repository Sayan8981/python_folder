# # import oops_concept

# # str_ = "My Name is Sakthi"

# # print(str_[::-1]) 

# # letter_list = list()

# #     #import pdb;pdb.set_trace()
# #     letter_list.append(str_[letter])
# # print (letter_list)

# # for letter in range(len(str_)-1,-1,-1):
# # print ("".join(letter_list))

# # class A(object):
# #     def __init__(self):
# #         if getattr(self.__class__, '_has_instance', False):
# #             raise RuntimeError('Cannot create another instance')
# #         self.__class__._has_instance = True
# #         print ("hi i ma boy")


# # obj1 = A()

# # obj2 = A()


# #monkey_patching
# class GeeksClass:
#     def function(self):
#         print ("function()")

# #import pdb
# def monkey_function(self):
#     print ("monkey_function()")
 
# GeeksClass.function = monkey_function
# obj = GeeksClass()
# obj.function()


# list1 = [True, False, True]
# #works as OR operator 
# print (any(list1))
# #works as AND operator 
# print(all(list1))


# import pickle

# # Define a Python object
# person = {
#     "name": "Alice",
#     "age": 30,
#     "gender": "female"
# }
 
# # Pickle the object to a binary file
# with open("person.pickle", "wb") as file:
#     pickle.dump(person, file)
 
# print("Pickling completed")


# # load the data from a file
# with open('person.pickle', 'rb') as f:
#     data = pickle.load(f)
 
# # print the data
# print(data)

# names = ["Jacob", "Joe", "Jim"] 
  
# #walrus operator
# if (name := input("Enter a name: ")) in names: 
#     print(f"Hello, {name}!") 
# else: 
#     print("Name not found.")
    
# sample_data = [
#     {"userId": 1,  "name": "rahul", "completed": False},
#     {"userId": 1, "name": "rohit", "completed": False},
#     {"userId": 1,  "name": "ram", "completed": False},
#     {"userId": 1,  "name": "ravan", "completed": True}
# ]

# for data in sample_data:
#     if name := data.get("name"):
#         print (name)
#     # if data.get("name"):
#     #     print (data.get("name"))   
    
# class X:
#     def __init__(self):
#         self.__num1 = 5
#         self.num2 = 2

#     def display_values(self):
#         print(self.__num1, self.num2)
# class Y(X):
#     def __init__(self):
#         super().__init__()
#         self.__num1 = 1
#         self.num2 = 6 
# obj = Y()
# obj.display_values() 
            

list_ = [x for x in range (1,50)]
print (list_)
my_dict = {i:1+7 for i in range(1, 10)}
print (my_dict)

list1 = [2, 33, 222, 14, 25]
print (list1[::3])
list1.sort()

print (list1)



# def Star_triangle(n):
#     for x in range(n):
#         #import pdb;pdb.set_trace()
#         print(' '*(n-x-1)+'*'*(2*x+1))
 
# Star_triangle(14)

import pandas as pd
data = pd.DataFrame([[65, 158], [92, 183]],
                      index=['Ramesh', 'Suresh'],
                      columns=['weight', 'height'])
print (data.stack())

a = [4,2,4,2,1,6,7,78,3,2,8,0,10]
a.sort()
print (a)
class CSStudent: 
  
    # Class Variable 
    stream = 'cse'             
  
    # The init method or parameterized constructor 
    def __init__(self, roll): 
    
        # Instance Variable     
        self.roll = roll        
    
# Objects of CSStudent class 
obj = CSStudent(101) 
b = CSStudent(102) 

# print(obj.stream)  # prints "cse" 
# print(b.stream)  # prints "cse" 
# print(obj.roll)    # prints 101 
   
# Class variables can be accessed using class 
# name also 
# print(CSStudent.stream) # prints "cse" 


#Inheritance


#parent class
class Bird(object):
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super(Penguin, self).__init__()
        print("Penguin is ready")
        super(Penguin, self).whoisThis()

    def whoisThis(self):
        self.swim()
        print("Penguin")
        

    def run(self):
        print("Run faster")

peggy = Penguin()

peggy.whoisThis()
peggy.swim()
peggy.run()

#Encapsulation

# class Computer:

#     def __init__(self):
#         self.__maxprice = 900

#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))

#     def setMaxPrice(self, price):
#         self.__maxprice = price

# c = Computer()
# c.sell()

# # change the price
# c.__maxprice = 1000
# c.sell()

# # using setter function
# c.setMaxPrice(1000)
# c.sell()

#Polymorphism

# class Parrot:

#     def fly(self):
#         print("Parrot can fly")
    
#     def swim(self):
#         print("Parrot can't swim")

# class Penguin:

#     def fly(self):
#         print("Penguin can't fly")
    
#     def swim(self):
#         print("Penguin can swim")

# # common interface
# def flying_test(bird):
#     bird.fly()

# #instantiate objects
# blu = Parrot()
# peggy = Penguin()

# # passing the object
# flying_test(blu)
# flying_test(peggy)

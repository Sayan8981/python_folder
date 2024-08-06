
# num = int(input("Enter a number for factorial:"))
# factorial_num = num

# for index in range (num-1,0,-1):
#     factorial_num = factorial_num * index

# print (factorial_num)
import math

def factorial(x):
    if x <= 1:
       return 1
    else:
        return x * factorial(x-1)
    
print (factorial(6))    

print (math.factorial(6))
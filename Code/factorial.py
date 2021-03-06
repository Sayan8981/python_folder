
num = int(input("Enter a number for factorial:"))
factorial_num = num

for index in range (num-1,0,-1):
    factorial_num = factorial_num * index

print (factorial_num)
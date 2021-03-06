
num1 = 23

num2 = 25

max_num = max(num1, num2)

print (max_num)

if num1 > num2:
    print (num1)
else:
    print (num2)

#max from list of numbers:

list_num = [2,34,2022,20,56,34,10,100,28,48,90,200,2021,9]
empty_arr = [0]

print ("length list:", len(list_num), list_num)

for index in range(0, len(list_num)):# 0-9
    for i in range(index+1, len(list_num)):
        if list_num[i] > list_num[i-1]:
            if list_num[i] > empty_arr[0]:
                empty_arr[0] = list_num[i]

print ("max_number:", empty_arr[:])            




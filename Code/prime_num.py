#Python program to print all Prime numbers in an Interval; not considering from 0 limit 

start_limit = int(input("Enter the start number :"))
end_limit = int(input("Enter the end number :"))

for num in range(start_limit,end_limit+1):
    if num > 0:
        for index in range(2,num):
            if (num % index == 0):
                break
        else:
            print (num)


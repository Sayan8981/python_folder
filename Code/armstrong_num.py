
from pdb import set_trace


num = int(input("Enter the number: "))

def length_num(num):
    power = 0
    while (num>0):
        num = num//10
        power += 1
    return power    

def armstrong_number(num):
    length_number = length_num(num)
    armstrong_num = 0
    input_num = num
    while (num>0):
        rem = num%10
        num = num//10
        armstrong_num = armstrong_num + pow(rem,length_number)
    if armstrong_num == input_num:
        return ("%s is armstrong number."%input_num)
    else:
        return ("%s is not armstrong number."%input_num)    

if __name__ == '__main__':
    print (armstrong_number(num))

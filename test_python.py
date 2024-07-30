# ## to get find out maximum profit from price_list with price_list first_index = buy and second index = sell respectively.

# price_list = [500,120,130,250,100,80]
# profit_dict = dict()

# for price_index in range(0,len(price_list)):
#     buy_price = price_list[price_index]
#     while price_index < len(price_list) - 1:
#         price_index += 1
#         sell_price = price_list[price_index]
#         temp_profit = sell_price - buy_price
#         if (sell_price - buy_price) > 0 or (sell_price - buy_price) > temp_profit:
#             profit_dict.update ({"%s"%price_index: sell_price - buy_price})

# print ({str(max(profit_dict,key = lambda x: profit_dict[x])): profit_dict.get(max(profit_dict,key = lambda x: profit_dict[x]))})   


# class Solution(object):

#     def __init__(self):
#         self.string_1 = '' #ab
#         self.string_2 = '' #pqrs
#         self.string_ = ''  #apbqrs

#     def mergeAlternately(self, word1, word2):
#         if word1 and word2:
#             if len(word1) >= 1 and len(word2) <=100:
#                 if len(word1) <= len(word2):
#                     for length in range(0, len(word2)):
#                         try:
#                             self.string_1 = word1[length]
#                             self.string_2 = self.string_1 + word2[length]
#                         except Exception:
#                             self.string_2 = word2[length:] 
#                             self.string_ = self.string_ + self.string_2
#                             break   
                               
#                         self.string_ = self.string_ + self.string_2

                    
#         return self.string_
    
# print (Solution().mergeAlternately("ab", "pqrs"))


def cal(num):
    return num*num

Number = [2,3,4,5,7,8,9]
result = map(cal, Number)

for item in result:
    print(item)     
    
# Driver code to test above
arr = [25, 34, 47, 21, 22, 11, 37]    
arr.sort()
print (arr)
length = len(arr)

for i in range(length-1):
    for j in range(length-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
         
print (arr)        

for i in range(0,5):
    print (' '*(5-i-1)+'*'*(2*i+1))    
    
def armstrng(n):
    sum_ =0
    temp = n
    #import pdb;pdb.set_trace()
    while temp > 0:
        x = temp % 10
        sum_ = sum_ + x**3
        temp = temp // 10

    print ("armstrong") if sum_ == n else print("not armstrong")
armstrng(153)            

def fibbo(series):
    fib_series = [0, 1]
    for i in range (2, series):
        next_series = fib_series[-1] + fib_series[-2]
        fib_series.append(next_series)
    return fib_series[:series]    
        
print (fibbo(10))    

def fibbo(series):
    a , b = 0, 1
    for i in range (series):
        yield a
        a, b = b, a+b      
        
print (list(fibbo(20)))    
        
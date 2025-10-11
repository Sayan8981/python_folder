list_ = [1,1, 3, 2, 4, 3, 2, 2, 2, 5, 5,88,5,4]

from collections import Counter

frequency = Counter(list_)
most_common_element, count = frequency.most_common(1)[0]
print (f"most_common_ele: {most_common_element} , count : {count}")


num = 1232

num = list(str(num))
print (int("".join(num[::-1])))

class list_node(object):
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def hascycle(self, head: list_node) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False    
    
array_ = [1, 2, 2, 3, 3, 4, 3]
print (sorted(array_))
originl_array = set(sorted(array_))
print (list(originl_array))



def profit_list(price_list: list):
    profit_dict = dict()
    #iterate through the price listed 
    for price_index in range(0,len(price_list)):
        #to retrive the buy price
        buy_price = price_list[price_index]
        #to check the price index is less than the length of the price listed 
        while price_index < len(price_list) - 1:
            price_index += 1 #incremental of price index
            sell_price = price_list[price_index] #to get the sell price index
            temp_profit = sell_price - buy_price
            if temp_profit > 0:
                profit_dict.update ({"%s"%price_index: temp_profit})
               
    return profit_dict  

          
price_list = [10,9,16,17,19,23]#[500,120,130,250,100,80]
profit_dict = profit_list(price_list=price_list)

#to get the maximum profit
print ({str(max(profit_dict,key = lambda x: profit_dict[x])): profit_dict.get(max(profit_dict,key = lambda x: profit_dict[x]))}) 
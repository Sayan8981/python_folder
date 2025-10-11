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
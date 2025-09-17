class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    """Convert a Python list into a linked list and return its head"""
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    """Convert a linked list back to a Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def addTwoNumbers(l1, l2):
    """Add two numbers represented by linked lists"""
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next

# --------------------------
# Test the code
# --------------------------
# 342 (2→4→3) + 465 (5→6→4) = 807 (7→0→8)
l1 = build_linked_list([2, 4, 3])
l2 = build_linked_list([5, 6, 4])

result = addTwoNumbers(l1, l2)
print(linked_list_to_list(result))  # Output: [7, 0, 8]
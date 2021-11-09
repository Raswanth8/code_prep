# Add two numbers problem
# Add values and carry
# 8+7 = 15 (5->1) (special case)

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        cur = temp
        
        carry = 0
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0 # or carry in loop is handle the special case
            v2 = l2.val if l2 else 0
            
            
            val = v1+v2+carry  # New value
            carry = val//10
            val = val %10
            cur.next = ListNode(val)
            
            cur = cur.next   # Updating pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next
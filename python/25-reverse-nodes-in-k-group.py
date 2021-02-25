# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
break problem 
1) given k-node return reversed one
2) find k node, reverse it using function 1) and stitch this to the next k-node
"""


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        origin_head = None
        
        (can_reverse, next_head) = self.hasK(head, k)
        prev_tail = None
        while can_reverse:
            (reversed_head, reversed_tail) = self.reverseK(head, k)
            if prev_tail:
                prev_tail.next = reversed_head
            if not origin_head: # one time
                origin_head = reversed_head
            
            prev_tail = reversed_tail
            
            head = next_head
            (can_reverse, next_head) = self.hasK(head, k)
            
        if prev_tail:
            prev_tail.next = head
            
        return origin_head
            
        
    def hasK(self, head, k):
        for i in range(k):
            if not head:
                return (False, None)
            head = head.next
        
        return (True, head)
        
        
    def reverseK(self, head, k):
        tail = head
        
        prev = None
        curr = head
        for i in range(k):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            
        return (prev, tail)
            
                
                
                
                
                
                
            
        

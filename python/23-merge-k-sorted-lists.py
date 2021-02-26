# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        heads = lists
        
        # initialize heap. each element looks like (value, index of list it came from, pointer of node)
        h = []        
        for (i, node) in enumerate(heads):
            if not node:
                continue
            h.append((node.val, i, node))
            heads[i] = node.next
            
        heapq.heapify(h)
        
        head = None
        tail = None

        while h:
            (val, i, node) = heapq.heappop(h)
            if heads[i]:
                heapq.heappush(h, (heads[i].val, i, heads[i]))
                heads[i] = heads[i].next
            
            if not head:
                head = node
            if tail:
                tail.next = node
            tail = node
        if tail:
            tail.next = None
        
        return head
            
            
            
            
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
more complicated example..

      1
    2   3 
   4  5
  
  voyage 1 3 2 4 5

"""

from collections import deque

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        self.i=0
        
        def sol(r):
            if not r:
                return []
            if r.val != voyage[self.i]:
                return [-1]
            
            self.i += 1
            child = []
            if r.left and not r.right:
                child = sol(r.left)
            elif not r.left and r.right:
                child = sol(r.right)
            elif not r.left and not r.right:
                child = []
            else:
                if r.left.val != voyage[self.i]:
                    child = sol(r.right) + sol(r.left) + [r.val]
                else:
                    child = sol(r.left) + sol(r.right)
            
            if -1 in child:
                return [-1]
            return child
        
        
        return sol(root)
        
        
                
            
                
            
            

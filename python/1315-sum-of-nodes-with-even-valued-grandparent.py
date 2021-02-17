# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        
        def sol(root, isParentEven, isGrandParentEven):
            if not root:
                return 0
            
            isRootEven = root.val % 2 == 0
            
            ans = 0
            if isGrandParentEven:
                ans = root.val
            
            return ans + sol(root.left, isRootEven, isParentEven) + sol(root.right, isRootEven, isParentEven)
        
        return sol(root, False, False)
        

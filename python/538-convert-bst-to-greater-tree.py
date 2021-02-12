# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        root = self.helper(root, 0)
        
        return root
        
    def helper(self, root, sumLarger):
        if root.right:
            root.right = self.helper(root.right, sumLarger)
            root.val += self.get_leftmost(root.right).val
        else:
            root.val += sumLarger
        
        if root.left:
            root.left = self.helper(root.left, root.val)
            
        return root

        
    def get_leftmost(self, root):
        if root.left:
            return self.get_leftmost(root.left)
        return root

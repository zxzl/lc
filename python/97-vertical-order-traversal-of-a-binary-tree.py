# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        ans = defaultdict(list)
        
        q = deque()
        q.append((root, 0))
        
        while q:
            level_size = len(q)
            level_ans = defaultdict(list)
            
            for _ in range(level_size):
                (node, c) = q.popleft()
                
                level_ans[c].append(node.val)
                
                if node.left:
                    q.append((node.left, c - 1))
                if node.right:
                    q.append((node.right, c+1))
                    
            # add to ans. sort if in same column
            for c in level_ans.keys():
                for val in sorted(level_ans[c]):
                    ans[c].append(val)
                    
        ans_list = []
        
        for c in sorted(ans.keys()):
            vals = ans[c]
            if len(vals) > 0:
                ans_list.append(vals)
                
        return ans_list
            
                
                
        

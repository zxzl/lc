"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        cloned = Node()
        cloned.val = root.val
        cloned.children = [
            self.cloneTree(child) for child in root.children
        ]
        return cloned
        

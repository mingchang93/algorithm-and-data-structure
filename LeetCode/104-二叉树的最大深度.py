# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):

        def find(node):
            if not node:
                return 0
            return 1 + max(find(node.left), find(node.right))
        
        return find(root)
    
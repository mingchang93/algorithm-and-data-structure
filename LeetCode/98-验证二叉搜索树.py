# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The idea is that performing in-order traversal gives a increasing sequence if the tree is indeed a binary search tree
"""
class Solution:
    def isValidBST(self, root):
        if not root: return True
        
        last = -float('inf')
        seq = self.inorderTraversal(root)
        for n in seq:
            if n > last:
                last = n
            else:
                return False
        return True

    def inorderTraversal(self, root):
        res = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            res.append(node.val)
            if node.right:
                traverse(node.right)
        
        if root:
            traverse(root)
        return res
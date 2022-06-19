# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """            

        def flatten_inner(node):
            if not node:
                return None
            dummy = TreeNode()
            dummy.right = node

            left, right = node.left, node.right
            node.left, node.right = None, None
            if left:
                node.right = flatten_inner(left)
                while node.right:
                    node = node.right
            if right:
                node.right = flatten_inner(right)
            return dummy.right

        root = flatten_inner(root)
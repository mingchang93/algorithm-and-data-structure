# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Recursively check if the left sub-tree and right sub-tree are symmetric
"""
class Solution:
    def isSymmetric(self, root):
        
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        
        return check(root, root)


"""
Level-order traversal: if symmetric, each level should be a Palindrome
"""
class Solution:
    def isSymmetric(self, root):
        queue = []

        if root:
            queue.append(root)
            while queue:
                temp_queue = []
                layer = []
                for node in queue:
                    if not node:
                        layer.append(None)
                        continue
                    temp_queue.append(node.left)
                    temp_queue.append(node.right)
                    layer.append(node.val)
                queue = temp_queue
                if layer != layer[::-1]:
                    return False
        
        return True
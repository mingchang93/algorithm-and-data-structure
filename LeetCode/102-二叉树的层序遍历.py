# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        res = []
        queue = []

        if root:
            queue.append(root)
            while queue:
                layer = []
                temp_queue = []
                for node in queue:
                    layer.append(node.val)
                    if node.left:
                        temp_queue.append(node.left)
                    if node.right:
                        temp_queue.append(node.right)
                queue = temp_queue
                res.append(layer)
        
        return res

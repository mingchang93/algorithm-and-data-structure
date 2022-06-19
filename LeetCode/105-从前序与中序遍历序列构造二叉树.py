# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
First attempt: exceeds maximum runtime
"""
class Solution:
    def buildTree(self, preorder, inorder):

        def reconstruct(preorder, inorder):
            if len(preorder) == 0 and len(inorder) == 0:
                return None
    
            root = TreeNode(preorder[0])
            for i in range(len(inorder)):
                if inorder[i] == root.val:
                    break
            left_inorder, right_inorder = inorder[:i], inorder[(i + 1):]

            left_preorder, right_preorder = [], []
            for p in preorder:
                if p in left_inorder:
                    left_preorder.append(p)
                if p in right_inorder:
                    right_preorder.append(p)
            
            root.left = reconstruct(left_preorder, left_inorder)
            root.right = reconstruct(right_preorder, right_inorder)
            return root
        
        return reconstruct(preorder, inorder)


"""
Second attempt: no need to loop over preorder to find the left preorder and right preorder, the preorder split index can be inferred from the inorder split index directly
"""
class Solution:
    def buildTree(self, preorder, inorder):

        def reconstruct(preorder, inorder):
            if len(preorder) == 0 and len(inorder) == 0:
                return None

            root = TreeNode(preorder[0])
            idx = inorder.index(root.val)
            left_inorder = inorder[:idx]
            right_inorder = inorder[(idx + 1):]

            left_preorder = preorder[1:(1 + idx)]
            right_preorder = preorder[(1 + idx):]


            root.left = reconstruct(left_preorder, left_inorder)
            root.right = reconstruct(right_preorder, right_inorder)
            return root
        
        return reconstruct(preorder, inorder)

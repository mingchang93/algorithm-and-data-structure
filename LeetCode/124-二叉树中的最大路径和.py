"""
NeetCode's solution
"""
class Solution:
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left_max = max(0, dfs(root.left))
            right_max = max(0, dfs(root.right))

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + left_max + right_max)

            # return max path sum WITHOUT split
            return root.val + max(left_max, right_max)
        
        dfs(root)
        return res[0]

class Solution:
    def subsets(self, nums):
        res = []

        def dfs(cur, l):
            res.append(cur)
            for i in range(l, len(nums)):
                dfs(cur + [nums[i]], i + 1)
        
        dfs([], 0)

        return res
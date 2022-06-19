"""
My first attempt: for a given n, we need to sum up the number of binary search trees constructeed by making i the root, i = 1, 2, ..., n

When i is the root: 
    1. count how many binary search trees can be formed using all the elements that are less than i, which consitutes to the left sub-tree
    2. count how many binary search trees can be formed using all the elements that are larger than i, which consitutes to the right sub-tree
    3. taking the product of the above two will give the total number of legal binary search trees by making i the root
"""
class Solution:
    def numTrees(self, n):
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2

        for i in range(3, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[-1]

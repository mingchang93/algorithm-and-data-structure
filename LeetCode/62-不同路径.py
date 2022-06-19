"""
My first attempt: solved by DP
Transition: DP[i][j] = DP[i - 1][j] + DP[i][j - 1]
Memory optimization: use only O(n) space to store the DP table
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        temp_dp = [0] * n
        temp_dp[0] = 1

        for _ in range(m - 1):
            for j in range(1, n):
                temp_dp[j] = dp[j] + temp_dp[j - 1]
            
            dp = temp_dp

        return dp[-1]
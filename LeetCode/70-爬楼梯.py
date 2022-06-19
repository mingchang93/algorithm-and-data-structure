"""
DP problem: 
# ways to reach position i = 
    # ways to reach position i-1 +
    # ways to reach position i-2

Memory can also be optimized to just use 3 variables to store the dp
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        t1, t2, t3 = 1, 2, 0

        for _ in range(2, n):
            t3 = t1 + t2
            t1, t2 = t2, t3
        
        return t3
"""
NeetCode's solution: dynamic programming approach: 
1. Maintain two variables cur_max and cur_min
2. When encountering a negative number, we could potentially turn the cur_min into cur_max
3. When encountering a zero, ignore it by resetting cur_max and cur_min to 1

Transition function:
cur_max = max(n * cur_max, n * cur_min, n) # when both cur_max and cur_min negative, and n is positive
cur_min = min(n * cur_max, n * cur_min, n) # the opposite of the above case
"""


class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        cur_max, cur_min = 1, 1

        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
            
            tmp_max, tmp_min = n * cur_max, n * cur_min
            cur_max = max(tmp_max, tmp_min, n)
            cur_min = min(tmp_max, tmp_min, n)
            res = max(cur_max, res)

        return res

"""
Binary search
"""


import math


class Solution:
    def minEatingSpeed(self, piles, h):
        if len(piles) == h:
            return max(piles)

        def check(k):
            return sum([math.ceil(p / k) for p in piles]) <= h

        lower, upper = 1, max(piles)
        while lower < upper:
            mid = lower + (upper - lower) // 2

            
            if check(mid):
                upper = mid # can finish, set the new upper = mid
            else:
                lower = mid + 1 # cannot finish, set the new lower = mid + 1
            
        return lower

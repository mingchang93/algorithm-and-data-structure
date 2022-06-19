"""
NeetCode's solution: at each position, find the maximum heights on both left and right sides. 
amount of water trapped at position i = min(left max at position i, right max at position i) - height at i
"""
class Solution:
    def trap(self, height):
        if not height: return 0

        res = 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]

        return res
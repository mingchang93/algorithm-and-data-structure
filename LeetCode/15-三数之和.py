"""
-4, -1, -1, 0, 1, 2

 0,  1,  2, 3, 4, 5

i = 0:
    left = 1, right = 5, sum = -4 + -1 + 2 = -3 < 0
    left = 2, right = 5, sum = -4 + -1 + 2 = -3 < 0
    left = 3, right = 5, sum = -4 +  0 + 2 = -2 < 0
    left = 4, right = 5, sum = -4 +  1 + 2 = -1 < 0

i = 1:
    left = 2, right = 5, sum = -1 + -1 + 2 = 0
"""

import enum


class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

        return res
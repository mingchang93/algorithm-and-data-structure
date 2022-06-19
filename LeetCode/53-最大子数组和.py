"""
Main idea: any negative "prefix" does not contribute to the sum of the subarray, 
so discard any negative "prefix" and start over at zero
"""
class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        presum = 0
        for i in nums:
            if presum < 0:
                presum = i
            else:
                presum += i
            res = max(presum, res)
        return res
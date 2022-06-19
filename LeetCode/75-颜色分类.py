"""
My first attempt: loop the entire array twice. First time to sort zeros, 
second time to sort the twos
"""
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                while nums[zero_idx] == 0 and i != zero_idx:
                    zero_idx += 1
                nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
            
        two_idx = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 2:
                while nums[two_idx] == 2 and i != two_idx:
                    two_idx -= 1
                nums[two_idx], nums[i] = nums[i], nums[two_idx]


"""
NeetCode's solution, only needs one pass
"""
class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            if nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1
            i += 1
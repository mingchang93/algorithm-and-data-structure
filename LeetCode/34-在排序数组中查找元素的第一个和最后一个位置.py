"""
NeetCode's solution

leftBiase = [True/False]
    True means we're searching for left boundary, keep searching on the left portion to find the left-most target value
    False means we're searching for right boundary, keep searching on the right portion find the right-most target value
"""
class Solution:
    def searchRange(self, nums, target):
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
        
    def binarySearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                res = mid
                if leftBias:
                    r = mid - 1
                else:
                    l = mid + 1
        return res
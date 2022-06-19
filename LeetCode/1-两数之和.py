class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            n = nums[i]
            if (target - n) in hashMap:
                return [hashMap[target - n], i]
            else:
                hashMap[n] = i
        return []

nums = [3,3]
target = 6
s = Solution()
print(s.twoSum(nums, target))
class Solution:
    def singleNumber(self, nums):
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for k, v in counts.items():
            if v == 1:
                return k

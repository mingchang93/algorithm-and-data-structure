"""
Time complexity: O(n * log(n) + n)
"""


class Solution:
    def topKFrequent(self, nums, k):
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        sorted_keys = sorted(counts, key=counts.get, reverse=True)
        return sorted_keys[:k]

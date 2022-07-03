import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.nums)

    def add(self, val):
        if len(self.nums) == self.k:
            cur = heapq.heappop(self.nums)
            new = max(cur, val)
        else:
            new = val
        heapq.heappush(self.nums, new)
        return self.nums[0]

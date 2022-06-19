"""
The idea is simple: if there is no zero in the array, then we can certainly reach the each.
If we encounter a zero, check if any previous cell contains a step size that can get us cross this zero.
"""
class Solution:
    def canJump(self, nums):
        if 0 not in nums[:-1]: return True
        
        i = len(nums) - 2
        while i >= 0 :
            if nums[i] == 0:
                for j in range(i - 1, -1, -1):
                    if i - j < nums[j]:
                        i = j - 1
                        break
                else:
                    return False
            else:
                i -= 1

        return True


"""
NeetCode has a better solution. Idea is similar: make the last element the goal, if we can reach the goal from the previous element, shift the goal to the previous element. If the goal is equal to 0 (at the first position), return True. Else, return False
"""
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
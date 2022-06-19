"""
Below is my attempt.
NeetCode has a slightly different solution: 
 1. remove the first element in nums
 2. generate the permutation of the remaining numbers
 3. add the first element back to the permutation from step 2
 4. add the first element back to nums
 5. recursively do step 1 - 4
"""
class Solution:
    def permute(self, nums):
        res = []

        def backtrack(perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return

            for n in nums:
                if n not in perm:
                    perm.append(n)
                    backtrack(perm)
                    perm.pop()
        
        backtrack([])

        return res
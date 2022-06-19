"""
My second attempt: don't always start at index 0, start where it left in the previous iteration
Same as NeetCode's idea, the solution is very similar but NeetCode is more memory efficient
"""
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(start_idx, cur_comb, new_target):
            if new_target == 0:
                res.append(cur_comb)
                return
            if new_target < candidates[0]:
                return
            
            for i in range(start_idx, len(candidates)):
                c = candidates[i]
                if c <= new_target:
                    dfs(i, cur_comb + [c], new_target - c)

        dfs(0, [], target)

        return res


"""
NeetCode's solution
"""
class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)

        return res



"""
My first attempt: gives the correct combinations, but have duplicates
"""
# class Solution:
#     def combinationSum(self, candidates, target):
#         res = []

#         def dfs(cur_comb, new_target):
#             if new_target == 0:
#                 res.append(cur_comb)
#                 return
#             if new_target < candidates[0]:
#                 return
            
#             for c in candidates:
#                 if c <= new_target:
#                     dfs(cur_comb + [c], new_target - c)

#         dfs([], target)

#         return res
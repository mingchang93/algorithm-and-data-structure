"""
Three scenarios in total:
    1. Only add "(" if #opening parenthese < n
    2. Only add ")" if number of closed parenthese < #open
    3. The string is valid if #open == #closed == n

Below is my DFS solution
"""
class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(num_open, num_close, cur_str):
            if num_open == n and num_close == n:
                res.append(cur_str)
                return
            
            if num_open == num_close:
                dfs(num_open + 1, num_close, cur_str + '(')
            
            if num_open < n and num_open > num_close:
                dfs(num_open + 1, num_close, cur_str + '(')
                dfs(num_open, num_close + 1, cur_str + ')')
            
            if num_open == n and num_open > num_close:
                dfs(num_open, num_close + 1, cur_str + ')')

        dfs(0, 0, '')

        return res

"""
NeetCode's backtracking solution
"""
class Solution:
    def generateParenthesis(self, n):
        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append(''.join(stack))
            
            if openN < n:
                stack.append('(')
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)

        return res

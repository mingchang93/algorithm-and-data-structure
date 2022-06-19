"""
Below solution can pass, but inefficient in BOTH time and space complexity

See 4 more solutions from LeetCode official solution
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        indicators = [0 for _ in range(len(s))]
        stack = []

        for i, c in enumerate(s):
            if c == ')':
                if stack and stack[-1][0] == '(':
                    indicators[stack[-1][1]] = 1
                    indicators[i] = 1
                    stack.pop()
            else:
                stack.append((c, i))
        
        max_len = 0
        temp_len = 0
        for j in indicators:
            if j == 0:
                temp_len = 0
            else:
                temp_len += 1
            max_len = max(max_len, temp_len)
        
        return max_len
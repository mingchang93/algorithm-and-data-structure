"""
NeetCode has a much neater solution down below this one.
"""
class Solution:
    def isValid(self, s):
        if s == '':
            return False
        if len(s) % 2 != 0:
            return False

        brackets_pair = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for bracket in s:
            if bracket in brackets_pair:
                stack.append(bracket)
            else:
                try:
                    last_bracket = stack.pop()
                except IndexError:
                    return False

                if bracket != brackets_pair[last_bracket]:
                    return False

        if stack:
            return False

        return True

"""
Same idea, but NeetCode's solution is much neater
"""
class Solution:
    def isValid(self, s):
        open_to_close = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for c in s:
            if c not in open_to_close:
                if stack and c == open_to_close[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
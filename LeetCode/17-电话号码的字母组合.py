from turtle import back


class Solution:
    def letterCombinations(self, digits):
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = ['']
        if digits == '':
            return []

        for digit in digits:
            res = [pre + suf for pre in res for suf in mapping[digit]]
        
        return res

"""
Backtracking solution from NeetCode
"""
class Solution:
    def letterCombinations(self, digits):
        digitsToChar = {
            '2': "abc",
            '3': "def", 
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return    
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        
        if digits:
            backtrack(0, '')

        return res
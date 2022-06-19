"""
Solution 1: NeetCode, iterate through every character in the string
At every character, make it the center and check for Palindrome
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        max_len = 0
        res = ""            

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:(r + 1)]
                l -= 1
                r += 1

            # even length
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > max_len:
                    max_len = r - l + 1
                    res = s[l:(r + 1)]
                l -= 1
                r += 1
        
        return res


"""
Soultion 2: Dynamic programming
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 1:
            return s

        max_len = 1
        begin_index = 0
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        for j in range(1, len(s)):
            for i in range(j):
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    if j - i <= 2:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
        
                if dp[i][j] == 1 and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    begin_index = i

        return s[begin_index:(begin_index + max_len)]
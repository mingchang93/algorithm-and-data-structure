"""
Brute-force solution, check every possible solution
"""
class Solution:
    def maxArea(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                temp_area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, temp_area)
        return max_area


"""
Actual solution. 
Hint on this problem: there are two scenarios:
    Scenario 1: the width is very long but the length is relatively short, in this way, we can still get a large area
    Scenario 2: the width is short but the length is very long, we can also get a large are this way
    Hence, we can trade off width and height to get maximum are.

Overall strategy: start with maximum width, each time, move the shorter vertical line (out of the current two) to the next position. This way, we are keeping longer length and changing the width to see if we can get a larger area
"""
class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, 
                           (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
            

height = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(height))

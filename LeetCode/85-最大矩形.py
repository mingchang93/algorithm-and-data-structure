class Solution:
    def maximalRectangle(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        maxArea = 0
        prev_heights = [0] * cols
        for i in range(rows):
            curr_heights = [0] * cols
            for j in range(cols):
                if matrix[i][j] == "1":
                    curr_heights[j] = prev_heights[j] + 1
            prev_heights = curr_heights
            maxArea = max(maxArea, self.largestRectangleArea(curr_heights))
        return maxArea

    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

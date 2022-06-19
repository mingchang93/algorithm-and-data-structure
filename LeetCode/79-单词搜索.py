class Solution:
    def exist(self, board, word):

        def generate_coord(i, j):
            res = []
            if i > 0: res.append([i - 1, j])
            if i < m - 1: res.append([i + 1, j])
            if j > 0: res.append([i, j - 1])
            if j < n - 1: res.append([i, j + 1])
            return res

        def backtrack(i, j, k):
            if k == len(word): 
                all_paths.append(path)
                return

            for ii, jj in generate_coord(i, j):
                if visited[ii][jj] != 1 and board[ii][jj] == word[k]:
                    visited[ii][jj] = 1
                    path.append([ii, jj])
                    backtrack(ii, jj, k + 1)
                    path.pop()
                    visited[ii][jj] = 0

        m, n = len(board), len(board[0])
        visited = [[0] * n for _ in range(m)]
        all_paths = []
        path = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    path.append([i, j])
                    backtrack(i, j, 1)
                    if all_paths: return True
                    path = []
                    visited = [[0] * n for _ in range(m)]

        return False

"""
NeetCode's solution: same logic but much more neet
"""
class Solution:
    def exist(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
        
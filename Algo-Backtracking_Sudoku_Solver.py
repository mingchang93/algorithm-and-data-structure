def solve():
    global grid

    def possible(x, y, n):    
        for i in range(9): # check if n is already in the row
            if grid[x][i] == n:
                return False
        for i in range(9): # check if n is already in the column
            if grid[i][y] == n:
                return False
        x0 = (x // 3) * 3 # check if n is already in the 3x3 subgrid
        y0 = (y // 3) * 3 # coordinates of the upper left most cell
        for i in range(3):
            for j in range(3):
                if grid[x0+i][y0+j] == n:
                    return False
        return True

    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[x][y] = n
                        solve()
                        grid[x][y] = 0
                return # if none of the choices of n works, return
    printGrid(grid)

import pprint
def printGrid(grid):
    pprint.pprint(grid)

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
printGrid(grid)
print('Solved:------------------')
solve()

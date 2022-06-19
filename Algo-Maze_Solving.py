'''
Python program to find the shortest path between a given source cell to a destination cell.

https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
'''
# %%
from collections import deque

# To store matrix cell coordinates
class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt, dist):
        self.pt = pt # The coordinates of the cell
        self.dist = dist # Cell's distance from the source

# Function to find the shortest path between
# a given source cell to a destination cell.
def BFS(mat, src, dest):

    # These arrays are used to get row and column
    # numbers of 4 neighbours of a given cell
    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]

    ROW, COL = len(mat), len(mat[0])

    # Check whether given cell(row, col)
    # is a valid cell or not
    def isValid(row, col):
        return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)
    
    # check source and destination cell
    # of the matrix have value 1
    if mat[src.x][src.y] != 1 or mat[dest.x][dest.y] != 1:
        return -1
    
    visited = [[False for i in range(COL)] for j in range(ROW)]
    
    # Mark the source cell as visited
    visited[src.x][src.y] = True
    
    # Create a queue for BFS
    q = deque()
    
    # Distance of source cell is 0
    s = queueNode(src, 0)
    q.append(s) # Enqueue source cell
    
    # Do a BFS starting from source cell
    while q:

        curr = q.popleft() # Dequeue the front cell
        
        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        
        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]
            
            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if (isValid(row, col) and mat[row][col] == 1 and not visited[row][col]):
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col), curr.dist + 1)
                q.append(Adjcell)
    
    # Return -1 if destination cannot be reached
    return -1


mat = [[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
        [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
        [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
        [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
        [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
        [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
        [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
        [ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]

source, dest = Point(0, 0), Point(3, 4)

dist = BFS(mat, source, dest)

if dist != -1:
    print("Shortest Path is", dist)
else:
    print("Shortest Path doesn't exist")

# %%

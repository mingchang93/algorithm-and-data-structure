'''
Depth first search

https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

Go deep; can be implemented in recursive manner or interative manner (using a stack)
'''

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSRecurUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSRecurUtil(neighbor, visited)
    
    def DFSRecur(self, v):
        visited = set()
        self.DFSRecurUtil(v, visited)


from collections import deque

class Graph:
    def __init__(self, V):
        self.V = V # numebr of vertices
        self.adj = [[] for _ in range(self.V)] # adjacency list

    def addEdge(self, v, w):
        self.adj[v].append(w)

    def DFSIter(self, s):
        visited = [False for _ in range(self.V)] # visitied vector

        stack = deque()

        stack.append(s)

        while stack:
            s = stack.pop()
            
            if not visited[s]:
                print(s, end=' ')
                visited[s] = True
            
            for node in self.adj[s]:
                if not visited[node]:
                    stack.append(node)


g = Graph(5); # Total 5 vertices in graph
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(1, 4)
 
print("Following is Depth First Traversal")
g.DFSIter(0)

'''
Question: You are given 3 things. The root of a binary tree, a single start node in the binary tree, and a number k. Return all nodes that are k "hops" away from the start node in the binary tree. Return a list of the values held at those nodes.

https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/


Idea: 
    1. Do a DFS to store the edge between a parent node and the child node (in this way, we turn a directed graph, i.e., a binary tree, to an undirected graph)
    2. Since now the graph is undirected, do a normal BFS
'''
# %%
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def distanceK(root, target, k):

    def dfs(node, parent=None):
        if not node:
            return
        hashMap[node] = parent
        dfs(node.left, node)
        dfs(node.right, node)

    if root:
        # key is the node, value is the node's parent
        hashMap = {}
        dfs(root)

        current_level = 0
        queue = [target]
        visited = {target}
        while queue:
            tmp_queue = []
            for node in queue:
                for next_node in (node.left, node.right, hashMap[node]):
                    if next_node and next_node not in visited:
                        tmp_queue.append(next_node)
                        visited.add(next_node)
            current_level += 1
            if current_level == k:
                return [node.val for node in tmp_queue]
            queue = tmp_queue
    return []

node_0 = TreeNode(0)
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
node_8 = TreeNode(8)
root = node_3
root.left, root.right = node_5, node_1
node_5.left, node_5.right = node_6, node_2
node_2.left, node_2.right = node_7, node_4
node_1.left, node_1.right = node_0, node_8
print(distanceK(root, node_5, 2))
# %%

'''
Binary Tree Path:
Print out all the paths from root node to leaf nodes in a binary tree
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def getPaths(root):

    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]
    
    def DFS(node, current_path):
        if not node:
            return
        if not node.left and not node.right:
            all_paths.append(current_path + [node.val])
        else:
            DFS(node.left, current_path + [node.val])
            DFS(node.right, current_path + [node.val])

    all_paths, current_path = [], []
    DFS(root, current_path)
    
    return all_paths


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_3.right = node_5

print(getPaths(node_1))

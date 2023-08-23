import matplotlib.pyplot as plt
import networkx as nx

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def plot_tree(node, pos=None, parent=None, layer=0, tree=None):
    if pos is None:
        pos = {node: (0.5, 1.0)}
    else:
        x, y = pos[parent]
        x_shift = 0.5 / (2 ** (layer + 1))
        if node == parent.left:
            pos[node] = (x - x_shift, 1 - layer * 0.1)
        else:
            pos[node] = (x + x_shift, 1 - layer * 0.1)
    
    if tree is None:
        tree = nx.DiGraph()
        tree.add_node(node.val)
    
    if node.left:
        tree.add_edge(node.val, node.left.val)
        tree = plot_tree(node.left, pos, node, layer + 1, tree)
    
    if node.right:
        tree.add_edge(node.val, node.right.val)
        tree = plot_tree(node.right, pos, node, layer + 1, tree)
    
    return tree

# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

# Plot the binary tree
tree = plot_tree(root)
pos = nx.get_node_attributes(tree, 'pos')
nx.draw(tree, pos, with_labels=True, node_size=1000, node_color="skyblue")
plt.show()

# Cree una estructura de objetos que asemeje un Binary Tree.
# Debe incluir un método para hacer `print` de toda la estructura.
# No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class TreeNode: 
    data : str
    left : "TreeNode"
    right : "TreeNode"
    
    def __init__(self, data, node_left = None , node_right = None):
        self.data = data
        self.left = node_left
        self.right = node_right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        
    
    def print_tree(self, node):
        if node is None:
            return None
        
        print(f"This is the root {node.data}")
        if node.left:
            print(f"This is the first successor of {node.data}: {node.left.data}")
            self.print_tree(node.left)
        if node.right:
            print(f"This is the second successor of {node.data}: {node.right.data}")
            self.print_tree(node.right)


tree = BinaryTree(TreeNode("A"))
tree.root.left = TreeNode("B")
tree.root.right = TreeNode("C")

# Add D and E under B
tree.root.left.left = TreeNode("D")
tree.root.left.right = TreeNode("E")

tree.print_tree(tree.root)
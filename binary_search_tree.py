class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(
                    "The tree node {0} added to the left of {1} at depth {2}".format(value, self.value, self.depth + 1))
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value, self.depth + 1)
                print("Tree node {0} added to the right of {1} at depth {2}".format(value, self.value, self.depth + 1))
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        if value == self.value:
            return self
        elif self.left and value < self.value:
            return self.left.get_node_by_value(value)
        elif self.right and value >= self.value:
            return self.right.get_node_by_value(value)
        else:
            return None

    def depth_first_traversal(self):
        if self.left:
            self.left.depth_first_traversal()
        print("Depth={0}, Value={1}".format(self.depth, self.value))
        if self.right:
            self.right.depth_first_traversal()


root = BinarySearchTree(100)

# Insert values below:
root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

# Get nodes by value below:
print(root.get_node_by_value(75).value)
print(root.get_node_by_value(55))

tree = BinarySearchTree(48)
tree.insert(24)
tree.insert(55)
tree.insert(26)
tree.insert(38)
tree.insert(56)
tree.insert(74)

tree.depth_first_traversal()
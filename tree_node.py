class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding {0}".format(child_node.value))
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing {0} from {1}".format(child_node.value, self.value))
        self.children.remove(child_node)

    def traverse(self):
        nodes_to_visit = [self]
        while nodes_to_visit:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit.extend(current_node.children)


root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()

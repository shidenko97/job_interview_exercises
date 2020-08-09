"""Implementation of simple tree"""

import json
from typing import List


class Node:
    """Node of tree"""

    def __init__(self, *, value: int) -> None:
        self.value: int = value
        self.children: List[Node] = []

    def add_children(self, *, node) -> None:
        """
        Add a child to node's children.

        :param node: Node of new children
        :type node: Node
        :raise ValueError: Node has incorrect type
        """

        if not isinstance(node, Node):
            raise ValueError("Incorrect node type")

        self.children.append(node)

    def get_all_children(self) -> dict:
        """
        Recursively return all node's children.

        :return: All children of node
        :rtype: dict
        """

        return {
            str(child): child.get_all_children()
            for child in self.children
            if child
        }

    def __str__(self) -> str:
        return str(self.value)


class Tree:
    """Simple tree implementation"""

    def __init__(self, *, root: Node) -> None:
        self.root: Node = root

    def show(self) -> None:
        """Print tree in json format with indents."""

        root = self.root
        tree = {
            str(root): root.get_all_children()
        }
        formatted_tree = json.dumps(tree, indent=4)

        print(formatted_tree)


if __name__ == "__main__":
    root_node = Node(value=1)
    my_tree = Tree(root=root_node)

    my_tree.show()

    my_tree.root.add_children(node=Node(value=2))

    my_tree.show()

    my_tree.root.children[0].add_children(node=Node(value=3))

    my_tree.show()

    my_tree.root.add_children(node=Node(value=4))

    my_tree.show()

    # Trying to add third children to node in binary tree
    try:
        my_tree.root.add_children(node=5)
        my_tree.show()
    except ValueError:
        print("Incorrect type of node")
    else:
        raise ValueError("Why exception didn't raise??")

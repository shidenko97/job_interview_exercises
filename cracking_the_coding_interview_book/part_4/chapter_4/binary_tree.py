"""Implementation of binary tree (max 2 child per node), base on tree"""

from cracking_the_coding_interview_book.part_4.chapter_4.tree import Node, Tree


class BinaryTreeNode(Node):
    """Node of binary tree"""

    def add_children(self, *, node) -> None:
        """
        Add a child to node's children.

        :param node: Node of new children
        :type node: BinaryTreeNode
        :raise ValueError: Node has incorrect type
        :raise ValueError: Node already has 2 children
        """

        if len(self.children) >= 2:
            raise ValueError(
                "Binary tree's node can't have more than 2 children"
            )

        super().add_children(node=node)


class BinaryTree(Tree):
    """Binary tree implementation"""


if __name__ == "__main__":
    root_node = BinaryTreeNode(value=1)
    my_tree = BinaryTree(root=root_node)

    my_tree.show()

    my_tree.root.add_children(node=BinaryTreeNode(value=2))

    my_tree.show()

    my_tree.root.children[0].add_children(node=BinaryTreeNode(value=3))

    my_tree.show()

    my_tree.root.add_children(node=BinaryTreeNode(value=4))

    my_tree.show()

    # Trying to add third children to node in binary tree
    try:
        my_tree.root.add_children(node=BinaryTreeNode(value=5))
        my_tree.show()
    except ValueError:
        print("Can't add third children to node")
    else:
        raise ValueError("Why exception didn't raise??")

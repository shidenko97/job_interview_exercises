"""
Implementation of binary search tree (max 2 child per node),
sorted by value (less in left side, greater in right side)

Todo: is tree complete, is tree full, is tree perfect
tODO: in/pre/post order traversals
"""

from cracking_the_coding_interview_book.part_4.chapter_4.binary_tree import (
    BinaryTree, BinaryTreeNode
)


class BinarySearchTreeNode(BinaryTreeNode):
    """Node of binary search tree"""

    def __init__(self, *, value: int) -> None:
        super().__init__(value=value)
        self.left = None
        self.right = None

    def add_children(self, *, node) -> None:
        """
        Add a child to left or right child's node.

        :param node: Node of new children
        :type node: BinarySearchTreeNode
        :raise ValueError: Node has incorrect type
        """

        if not isinstance(node, BinarySearchTreeNode):
            raise ValueError("Incorrect node type")

        if self.value >= node.value:
            if self.left:
                self.left.add_children(node=node)
            else:
                self.left = node
                self.children.append(self.left)
        else:
            if self.right:
                self.right.add_children(node=node)
            else:
                self.right = node
                self.children.append(self.right)

    def find(self, *, value: int) -> bool:
        """
        Is specified value present in node's children.

        :param value: Value to search
        :type value: int
        :return: Result of search
        :rtype: bool
        """

        if self.value == value:
            return True
        elif self.left and self.value > value:
            return self.left.find(value=value)
        elif self.right and self.value < value:
            return self.right.find(value=value)
        return False


class BinarySearchTree(BinaryTree):
    """Binary search tree implementation"""

    def add_value(self, *, value: int) -> None:
        """
        Add value to tree.

        :param value: Value to adding
        :type value: int
        """

        self.root.add_children(node=BinarySearchTreeNode(value=value))

    def find(self, *, value) -> bool:
        """
        Is specified value present in binary search tree.

        :param value: Value to search
        :type value: int
        :return: Result of search
        :rtype: bool
        """

        return self.root.find(value=value)


if __name__ == "__main__":
    root_node = BinarySearchTreeNode(value=3)
    my_tree = BinarySearchTree(root=root_node)

    my_tree.show()

    my_tree.add_value(value=1)

    my_tree.show()

    my_tree.add_value(value=0)

    my_tree.show()

    my_tree.add_value(value=4)

    my_tree.show()

    my_tree.add_value(value=2)

    my_tree.show()

    print(my_tree.find(value=2))

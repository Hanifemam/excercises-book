class AVL:
    def __init__(self):
        self.root = None

    def left_rotation(self, node):
        pass

    def right_rotation(self, node):
        pass

    def balance_factor(self, node):
        if node:
            return node.left.height - node.right.height
        else:
            return 0

    def insert(self, val):
        pass

    def remove(self, val):
        pass


class Node:
    def __init__(self, val, height, left, right):
        self.val = val
        self.height = height
        self.left = left
        self.right = right

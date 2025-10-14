class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # use 1-based height; None -> 0


def height(n):
    return n.height if n else 0


def balance_factor(node):
    if not node:
        return 0
    else:
        return height(node.left) - height(node.right)


def update(n):
    n.height = 1 + max(height(n.left), height(n.right))
    return n


class AVL:
    def __init__(self):
        self.root = None

    def left_rotation(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        update(x)
        update(y)

        return y

    def right_rotation(self, x):
        y = x.left
        T3 = y.right

        y.right = x
        x.left = T3

        update(x)
        update(y)

        return y

    def insert(self, node, key):
        # (1) Standard BST insert
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node

        # (2) Update height
        update(node)

        # (3) Rebalance
        balance = balance_factor(node)

        # LL
        if balance > 1 and key < node.left.key:
            return self.right_rotation(node)

        # RR
        if balance < -1 and key > node.right.key:
            return self.left_rotation(node)

        # LR
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)

        # RL
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)

        return node

    def insert_key(self, key):
        self.root = self.insert(self.root, key)


if __name__ == "__main__":
    tree = AVL()
    root = None

    # Test sequences for different rotation cases
    tests = {
        "LL rotation": [30, 20, 10],
        "RR rotation": [10, 20, 30],
        "LR rotation": [30, 10, 20],
        "RL rotation": [10, 30, 20],
        "Mixed insertions": [50, 20, 70, 10, 30, 60, 80, 25, 27, 26],
    }

    def inorder(node):
        return inorder(node.left) + [node.key] + inorder(node.right) if node else []

    for name, seq in tests.items():
        tree = AVL()
        root = None
        for key in seq:
            root = tree.insert(root, key)
        print(f"\n{name}:")
        print("Inserted:", seq)
        print("Inorder traversal:", inorder(root))
        print("Root key:", root.key)
        print("Height:", root.height)

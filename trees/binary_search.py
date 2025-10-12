class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            new_node = Node(val)
            self.root = new_node
            return
        adding_position, parent, side = self.lookup(val)
        if adding_position:
            print(f"The {val} exists.")
            return
        else:
            new_node = Node(val)
            if side == "left":
                parent.left = new_node
            else:
                parent.right = new_node
            return new_node

    def lookup(self, val):
        curr = self.root
        parent = None
        side = None
        while curr:
            if val == curr.val:
                print(
                    f"{val} found. Left child value is {curr.left.val if curr.left else 'None'} and right child value {curr.right.val if curr.right else 'None'}"
                )
                return (curr, parent, side)
            elif val < curr.val:
                parent = curr
                side = "left"
                curr = curr.left
            elif val > curr.val:
                parent = curr
                side = "right"
                curr = curr.right

        print(f"{val} not found")
        return (None, parent, side)


# ---- test_bst.py ----

if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert some values
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    # Try inserting a duplicate
    bst.insert(7)

    # Look up existing and non-existing values
    bst.lookup(10)
    bst.lookup(7)
    bst.lookup(20)

    # Simple in-order traversal to verify structure
    def inorder(node):
        if node:
            inorder(node.left)
            print(node.val, end=" ")
            inorder(node.right)

    print("\nIn-order traversal (should be sorted):")
    inorder(bst.root)
    print()

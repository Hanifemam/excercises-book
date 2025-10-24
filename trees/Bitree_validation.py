# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traverse_list = []
        return True if inorder_DFS(root, traverse_list) else False


def inorder_DFS(root, traverse_list):
    if not root:
        return True

    # Traverse left subtree
    if not inorder_DFS(root.left, traverse_list):
        return False

    # Check current node
    if traverse_list and traverse_list[-1] >= root.val:
        return False
    traverse_list.append(root.val)

    # Traverse right subtree
    if not inorder_DFS(root.right, traverse_list):
        return False

    return True

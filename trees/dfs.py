from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from stack_queue.stack import Stack


def bfs(tree, root):
    stack = Stack()
    stack.push(root)
    traverse_list = []
    while stack.length > 0:
        next_root = stack.pop().val
        traverse_list.append(next_root)
        for child in tree[next_root]:
            stack.push(child)

    return traverse_list


tree = {
    "A": ["B", "C", "D"],
    "B": ["E", "F"],
    "C": ["G"],
    "D": [],
    "E": [],
    "F": ["H"],
    "G": [],
    "H": [],
}
root = "A"
print(bfs(tree, root))

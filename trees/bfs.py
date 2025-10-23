from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))
from stack_queue.queue import Queue


def bfs(tree, root):
    queue = Queue()
    queue.enqueue(root)
    traverse_list = []
    while queue.length > 0:
        next_root = queue.dequeue()
        traverse_list.append(next_root)
        for child in tree[next_root]:
            queue.enqueue(child)

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

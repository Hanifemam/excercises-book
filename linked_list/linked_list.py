class LinkedList:
    def __init__(self, value):
        node = Node(value, None, ind=0)
        self.head = node
        self.tail = node
        self.len = 1

    def append(self, value):
        node = Node(value, None, self.len)
        self.tail.next = node
        self.tail = node
        self.len += 1

    def prepend(self, value):
        node = Node(value, self.head, 0)
        self.head = node
        self.len += 1
        next_node = node.next
        while next_node:
            next_node.ind += 1
            next_node = next_node.next

    def insert(self, after_value, new_value):
        current = self.head
        while current:
            if current.value == after_value:
                node = Node(new_value, current.next, current.ind + 1)
                current.next = node
                current = current.next.next
                if self.tail is current:
                    self.tail = node
                while current:
                    current.ind += 1
                    current = current.next
                return
            current = current.next

        self.len += 1
        raise ValueError(f"{after_value} not found")

    def index_based_insert(self, ind, value):
        if ind < 0 or ind > self.len:
            raise ValueError(f"index {ind} out of range [0, {self.len}]")

        if ind == 0:
            self.prepend(value)
            return

        if ind == self.len:
            self.append(value)
            return

        pre_node, next_node = self.traverse(ind)
        if pre_node is None or next_node is None:
            raise ValueError(f"{ind} not found")

        node = Node(value, next_node, ind)
        pre_node.next = node
        runner = node.next
        while runner:
            runner.ind += 1
            runner = runner.next
        self.len += 1

    def traverse(self, ind):
        current_node = self.head
        current_ind = current_node.ind
        if current_ind == ind:
            return None, current_node
        next_node = current_node.next
        while next_node:
            if next_node.ind == ind:
                return current_node, next_node
            else:
                current_node = next_node
                next_node = current_node.next
        return None, None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


class Node:
    def __init__(self, value, next, ind):
        self._value = value
        self._next = next
        self._ind = ind

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def ind(self):
        return self._ind

    @ind.setter
    def ind(self, ind):
        self._ind = ind

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


# --- TEST SCRIPT ---
def print_list_with_indices(ll, title="List"):
    print(f"\n{title}:")
    node = ll.head
    out = []
    while node:
        out.append(f"({node.value},{node.ind})")
        node = node.next
    print(" -> ".join(out) + " -> None")
    print(f"len={ll.len}, head={ll.head.value}, tail={ll.tail.value}")


def validate_indices(ll):
    # ensure indices are 0..len-1 and in order
    node = ll.head
    expected = 0
    count = 0
    while node:
        assert (
            node.ind == expected
        ), f"Index mismatch at value {node.value}: {node.ind} != {expected}"
        expected += 1
        count += 1
        node = node.next
    assert count == ll.len, f"Length mismatch: counted {count}, ll.len={ll.len}"


if __name__ == "__main__":
    print("Creating linked list with head = 10...")
    ll = LinkedList(10)

    print("\nAppending values 20 and 30...")
    ll.append(20)
    ll.append(30)

    print("\nPrepending value 5...")
    ll.prepend(5)

    print_list_with_indices(ll, "Initial list")

    # ---------- index_based_insert tests ----------
    # 1) insert at head (ind == 0) -> acts like prepend
    print("\n[TEST] index_based_insert at ind=0 (prepend case)")
    ll.index_based_insert(0, 1)
    print_list_with_indices(ll, "After inserting 1 at ind=0")
    validate_indices(ll)

    # 2) insert in the middle (e.g., ind=3)
    print("\n[TEST] index_based_insert at ind=3 (middle insert)")
    ll.index_based_insert(3, 12)
    print_list_with_indices(ll, "After inserting 12 at ind=3")
    validate_indices(ll)

    # 3) insert before current tail (ind == tail.ind) — should insert BEFORE tail, not append
    print("\n[TEST] index_based_insert at ind=tail.ind (before tail)")
    tail_index_before = ll.tail.ind
    ll.index_based_insert(tail_index_before, 99)
    print_list_with_indices(
        ll, f"After inserting 99 at ind={tail_index_before} (before tail)"
    )
    validate_indices(ll)

    # 4) append at end (ind == len)
    print("\n[TEST] index_based_insert at ind=len (append case)")
    end_index = ll.len
    ll.index_based_insert(end_index, 100)
    print_list_with_indices(ll, f"After inserting 100 at ind={end_index} (append)")
    validate_indices(ll)

    # 5) out-of-range (ind == len + 1) -> should raise
    print("\n[TEST] index_based_insert out-of-range (should raise)")
    try:
        ll.index_based_insert(ll.len + 1, 12345)
    except ValueError as e:
        print(f"Raised as expected: {e}")

    # Final validations
    print("\nFinal validations...")
    validate_indices(ll)
    # quick sanity checks on head/tail
    assert ll.head.ind == 0, "Head index should be 0"
    # Ensure tail.ind == len-1
    assert ll.tail.ind == ll.len - 1, f"Tail index {ll.tail.ind} != len-1 {ll.len - 1}"

    print("\nAll index_based_insert tests passed ✅")

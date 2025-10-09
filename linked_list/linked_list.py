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

    def index_based_remove(self, ind):
        if ind < 0 or ind >= self.len:
            raise ValueError(f"index {ind} out of range [0, {self.len - 1}]")

        prev, curr = self.traverse_to_remove(ind)
        if curr is None:
            raise ValueError(f"index {ind} not found")

        if prev is None:
            self.head = curr.next
        else:
            prev.next = curr.next

        if curr.next is None:
            self.tail = prev

        runner = curr.next
        while runner:
            runner.ind -= 1
            runner = runner.next

        self.len -= 1
        if self.len == 0:
            self.head = None
            self.tail = None

    def traverse_to_remove(self, ind):
        if ind < 0 or ind >= self.len:
            return None, None

        prev = None
        curr = self.head
        while curr and curr.ind != ind:
            prev = curr
            curr = curr.next
        return prev, curr

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


# --- TEST SCRIPT ---
def print_list_with_indices(ll, title="List"):
    print(f"\n{title}:")
    node = ll.head
    out = []
    while node:
        out.append(f"({node.value},{node.ind})")
        node = node.next
    print(" -> ".join(out) + " -> None")
    if ll.len > 0:
        print(f"len={ll.len}, head={ll.head.value}, tail={ll.tail.value}")
    else:
        print(f"len={ll.len}, head=None, tail=None")


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
    if ll.len == 0:
        assert (
            ll.head is None and ll.tail is None
        ), "Empty list must have head=tail=None"
    else:
        assert ll.head.ind == 0, "Head index should be 0"
        assert (
            ll.tail.ind == ll.len - 1
        ), f"Tail index {ll.tail.ind} != len-1 {ll.len - 1}"


if __name__ == "__main__":
    print("Creating linked list with head = 10...")
    ll = LinkedList(10)

    print("\nAppending values 20 and 30...")
    ll.append(20)
    ll.append(30)

    print("\nPrepending value 5...")
    ll.prepend(5)

    # Optional: one index-based insert to have a richer structure
    print("\nIndex-based insert at ind=2 (insert 15 before current index 2)...")
    ll.index_based_insert(2, 15)  # Expect: 5(0),10(1),15(2),20(3),30(4)

    print_list_with_indices(ll, "Initial state before removals")
    validate_indices(ll)

    # --------- REMOVALS TESTS ---------

    # 1) Remove head (ind=0)
    print("\n[TEST] Remove head (ind=0)")
    ll.index_based_remove(0)
    print_list_with_indices(ll, "After removing head")
    validate_indices(ll)
    assert (
        ll.head is not None and ll.head.ind == 0
    ), "Head should exist and have ind=0 after head removal"

    # 2) Remove middle element (choose a valid middle index)
    mid_index = ll.len // 2
    print(f"\n[TEST] Remove middle (ind={mid_index})")
    ll.index_based_remove(mid_index)
    print_list_with_indices(ll, f"After removing index {mid_index}")
    validate_indices(ll)

    # 3) Remove tail (ind=len-1)
    tail_index = ll.len - 1
    print(f"\n[TEST] Remove tail (ind={tail_index})")
    old_tail_value = ll.tail.value
    ll.index_based_remove(tail_index)
    print_list_with_indices(ll, "After removing tail")
    validate_indices(ll)
    if ll.len > 0:
        assert (
            ll.tail.value != old_tail_value
        ), "Tail should have changed after removing old tail"

    # 4) Out-of-range removals
    print("\n[TEST] Remove with out-of-range indices (should raise)")
    try:
        ll.index_based_remove(-1)
    except ValueError as e:
        print("Raised as expected for -1:", e)
    try:
        ll.index_based_remove(ll.len)  # equal to len is invalid (valid range: 0..len-1)
    except ValueError as e:
        print(f"Raised as expected for ind==len ({ll.len}):", e)

    # 5) Remove everything until empty (always remove head for simplicity)
    print("\n[TEST] Remove everything until empty")
    while ll.len > 0:
        ll.index_based_remove(0)
        validate_indices(ll)
    print_list_with_indices(ll, "After removing all elements (should be empty)")
    assert (
        ll.head is None and ll.tail is None and ll.len == 0
    ), "List should be empty with head=tail=None"

    print("\nAll remove tests passed ✅")

class LinkedList:
    def __init__(self, value):
        node = Node(value, None, ind=0)
        self.head = node
        self.tail = node
        self.len = 1

    def append(self, value):
        node = Node(value, None, self.len)
        if self.tail:
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
        if current_node:
            current_ind = current_node.ind
        if current_ind == ind:
            return None, current_node
        if current_node:
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

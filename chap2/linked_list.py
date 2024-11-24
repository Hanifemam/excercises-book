class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __len__(self):
        return self.size

    def __iter__(self):
        next_node = self._head
        while next_node is not None:
            yield next_node.value
            next_node = next_node.next

    def insert(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
        if self._tail is not None:
            self._tail.next = node
        self._tail = node
        self.size += 1
        return node

    def get_at(self, index):
        current_node = self._head
        for i in range(index):
            if current_node is not None and current_node.next is not None:
                current_node = current_node.next
            else:
                print(f"{i} is out of linked list range")
                return None
        return current_node

    def set_at(self, index, value):
        node = self.get_at(index)
        node.value = value

    def delete_at(self, index, value):
        node = self.get_at(index)
        previous_node = self.get_at(index - 1)
        previous_node.next = node.next

    def insert_at(self, index, value):
        node = self.get_at(index - 1)
        if node is not None:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
            return new_node
        else:
            return None

    def delete_first(self):
        temp_node_value = self._head.value
        self._head = self._head.next
        self.size -= 1
        return temp_node_value

    def insert_first(self, value):
        node = Node(value)
        node.next = self._head
        self._head = node
        self.size += 1


class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

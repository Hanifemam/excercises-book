class LinkedList:
    def __init__(self, value):
        node = Node(value, None)
        self.head = node
        self.tail = node

    def append(self, value):
        node = Node(value, None)
        self.tail.next = node
        self.tail = node

    def prepend(self, value):
        next = self.head
        node = Node(value, next)
        self.head = node


class Node:
    def __init__(self, value, next):
        self.value = value
        self._next = next

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

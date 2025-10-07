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
        next_node = self.head
        node = Node(value, next_node)
        self.head = node

    def insert(self, index, value):
        pass

    def __iter__(self):
        self._cursor = self.head
        return self

    def __next__(self):
        if self._cursor:
            value = self._cursor.value
            self._cursor = self._cursor.next
            return value
        else:
            raise StopIteration


class Node:
    def __init__(self, value, next):
        self._value = value
        self._next = next

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


if __name__ == "__main__":
    print("Creating linked list with head = 10...")
    ll = LinkedList(10)

    print("\nAppending values 20 and 30...")
    ll.append(20)
    ll.append(30)

    print("Prepending value 5...")
    ll.prepend(5)

    print("\nIterating through the linked list:")
    for value in ll:
        print(value)

    print("\nIterating again (should still work):")
    for value in ll:
        print(value)

    print("\nManual iteration using next():")
    iterator = iter(ll)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        print("Reached end of list.")

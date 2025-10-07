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
        node = Node(value, self.head)
        self.head = node

    def insert(self, after_value, new_value):
        current = self.head
        while current:
            if current.value == after_value:
                node = Node(new_value, current.next)
                current.next = node
                if self.tail is current:
                    self.tail = node
                return
            current = current.next
        raise ValueError(f"{after_value} not found")

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


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


# --- TEST SCRIPT ---
if __name__ == "__main__":
    print("Creating linked list with head = 10...")
    ll = LinkedList(10)

    print("\nAppending values 20 and 30...")
    ll.append(20)
    ll.append(30)

    print("\nPrepending value 5...")
    ll.prepend(5)

    print("\nInitial list:")
    for value in ll:
        print(value, end=" -> ")
    print("None")

    print("\nInserting 15 after 10...")
    ll.insert(10, 15)

    print("Inserting 25 after 20...")
    ll.insert(20, 25)

    print("Inserting 35 after 30 (at tail)...")
    ll.insert(30, 35)

    print("\nList after insertions:")
    for value in ll:
        print(value, end=" -> ")
    print("None")

    print(f"\nHead: {ll.head.value}, Tail: {ll.tail.value}")

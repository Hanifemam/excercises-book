class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, val):
        if self.length == 0:
            node = Node(val)
            self.first = node
            self.last = node
        else:
            node = Node(val, next=self.last)
            if self.first == self.last:
                self.first.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.length > 1:
            val = self.first.val
            self.first = self.first.next
            self.length -= 1
            return val
        elif self.length == 1:
            val = self.last.val
            self.first = None
            self.last = None
            self.length = 0
            return val
        else:
            raise ValueError("Stack is empty")

    def peek(self):
        return self.last.val


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(2)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
# print(stack)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

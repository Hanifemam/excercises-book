class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, val):
        if self.top and self.bottom:
            node = Node(val)
            self.bottom = node
            self.top = node
        else:
            node = Node(val, next=self.top)
            self.top = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise ValueError("Stack is empty")
        if self.top and self.top == self.bottom:
            val = self.top.val
            self.top = None
            self.bottom = None
            self.length = 0
            return val
        else:
            val = self.top
            self.top = self.top.next
            self.length -= 1
            return val

    def peek(self):
        return self.top

    def __repr__(self):
        curr = self.top
        while curr:
            print(f"{curr.val} --> ")
            curr = curr.next


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
# print(stack)
stack.pop()
print(stack)

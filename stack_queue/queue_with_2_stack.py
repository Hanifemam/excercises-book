class MyQueue:

    def __init__(self):
        self.primary = Stack()
        self.secondary = Stack()

    def push(self, x: int) -> None:
        self.primary.push(x)

    def pop(self) -> int:
        while not self.primary.empty():
            self.secondary.push(self.primary.pop())
        holder = self.secondary.pop()
        while not self.secondary.empty():
            self.primary.push(self.secondary.pop())
        return holder

    def peek(self) -> int:
        while not self.primary.empty():
            self.secondary.push(self.primary.pop())
        holder = self.secondary.peek()
        while not self.secondary.empty():
            self.primary.push(self.secondary.pop())
        return holder

    def empty(self) -> bool:
        return self.primary.empty()


class Stack:
    def __init__(self):
        self.stack = []
        self.length = len(self.stack)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            False

    def push(self, val):
        self.stack.append(val)

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return False

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            raise ValueError("Stack is empty")
        else:
            return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.stack)
stack.pop()
print(stack.stack)

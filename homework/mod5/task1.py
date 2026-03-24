class Node:
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value, self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty")

        value = self.head.value
        self.head = self.head.previous
        return value

    def print(self):
        node = self.head
        values = []
        while node is not None:
            values.append(node.value)
            node = node.previous
        print(list(reversed(values)))


# Test:
stack = Stack()

try:
    stack.pop()
    print("Expected to throw exception, but passed") # this message shouldn't be printed
except Exception as e:
    print("Correct exception: " + e.args[0])

stack.push(1)
stack.push(2)
stack.push(4)
stack.print() # expected: [1, 2, 4]

stack.pop()
stack.push(3)
stack.print() # expected: [1, 2, 3]

stack.pop()
stack.print() # expected: [1, 2]
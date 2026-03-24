class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class Queue:
    def __init__(self):
        self.start = None
        self.end = None


    def enqueue(self, value):
        node = Node(value, previous=self.end)
        if self.end:
            self.end.next = node
        self.end = node
        if self.start is None:
            self.start = node


    def dequeue(self):
        node = self.start
        if node is None:
            raise Exception("Queue is empty")

        if id(node) == id(self.end):
            self.clear()
            return node.value

        self.start = node.next
        self.start.previous = None
        return node.value


    def insert(self, index, value):
        size = self.size()
        if index < 0 or index > size:
            raise IndexError(f"Index '{index}' is out of range")

        if size == 0 or index == size:
            self.enqueue(value)
            return

        if index == 0:
            node = Node(value, next=self.start)
            self.start.previous = node
            self.start = node
            return

        current = self.start
        for i in range(index):
            current = current.next

        previous = current.previous
        node = Node(value, previous=previous, next=current)
        previous.next = node
        current.previous = node


    def print(self):
        node = self.start
        values = []
        while node:
            values.append(node.value)
            node = node.next
        print(values)


    def size(self):
        count = 0
        node = self.start
        while node:
            count += 1
            node = node.next
        return count


    def clear(self):
        self.start = None
        self.end = None

# Test:
queue = Queue()

try:
    queue.dequeue()
    print("Expected to throw exception, but passed") # this message shouldn't be printed
except Exception as e:
    print("Correct exception: " + e.args[0])

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print() # [1, 2, 3]

queue.dequeue()
queue.print() # [2, 3]

queue.enqueue(4)
queue.print()  # [2, 3, 4]

queue.insert(0, 1)
queue.print() # [1, 2, 3, 4]

queue.insert(queue.size(), 5)
queue.print() # [1, 2, 3, 4, 5]

try:
    queue.insert(-1, 0)
    print("Expected to throw exception, but passed") # this message shouldn't be printed
except Exception as e:
    print("Correct exception: " + e.args[0])

try:
    queue.insert(queue.size() + 1, 7)
    print("Expected to throw exception, but passed") # this message shouldn't be printed
except Exception as e:
    print("Correct exception: " + e.args[0])
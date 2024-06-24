class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == self.capacity

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.items[-1]

if __name__ == '__main__':
    stack1 = Stack(capacity=5)

    stack1.push(1)

    stack1.push(2)

    print(stack1.is_full())
    # >> False

    print(stack1.top())
    # >> 2

    print(stack1.pop())
    # >> 2

    print(stack1.top())
    # >> 1

    print(stack1.pop())
    # >> 1

    print(stack1.is_empty())
    # >> True
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.items[0]
    
if __name__ == '__main__':
    queue1 = Queue(capacity=5)

    queue1.enqueue(1)

    queue1.enqueue(2)

    print(queue1.is_full())
    # >> False

    print(queue1.front())
    # >> 1

    print(queue1.dequeue())
    # >> 1

    print(queue1.front())
    # >> 2

    print(queue1.dequeue())
    # >> 2

    print(queue1.is_empty())
    # >> True
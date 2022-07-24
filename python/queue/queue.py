# FIFO
# Implement using deque

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()

    def isEmpty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(7)
    q.enqueue(19)
    q.enqueue(24)
    print(q.size())
    print(q.isEmpty())

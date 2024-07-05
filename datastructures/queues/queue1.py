#!/usr/bin/python3

from collections import deque 

class Queue: 
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return "Queue: " + str(list(self.items))
    
if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q)
    print(q.size())
    print(q.dequeue())
    print(q)
    print(q.peek())
    print(q.is_empty())


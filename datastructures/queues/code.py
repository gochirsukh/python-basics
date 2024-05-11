class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Append item to the end of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the first item from the queue
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        # Return the first item from the queue without removing it
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("Queue is empty")
            return None

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the number of items in the queue
        return len(self.queue)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue size:", q.size())  # Output: 3
print("Dequeue:", q.dequeue())  # Output: 1
print("Peek:", q.peek())        # Output: 2
print("Is empty:", q.is_empty())# Output: False

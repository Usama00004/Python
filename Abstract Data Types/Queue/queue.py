class Queue:
    def __init__(self):
        """Initialize an empty queue"""
        self.queue = []

    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the front item of the queue"""
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        """Return the front item of the queue without removing it"""
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue"""
        return len(self.queue)

    def display(self):
        """Display the current queue"""
        print("Current Queue:", self.queue)

    def __str__(self):
        """Return a string representation of the queue"""
        return f"Queue: {self.queue}"

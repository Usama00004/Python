class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack"""
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """Remove and return the top item of the stack"""
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped: {item}")
            return item
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        """Return the top item of the stack without removing it"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack"""
        return len(self.stack)

    def display(self):
        """Display the current stack"""
        print("Current Stack:", self.stack)


# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print(f"Top Element: {stack.peek()}")
    stack.pop()
    stack.display()
    print(f"Is Stack Empty? {stack.is_empty()}")
    print(f"Stack Size: {stack.size()}")

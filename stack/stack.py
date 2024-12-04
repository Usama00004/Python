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

    def sort_stack(self):
        """Sort a stack using one additional stack"""
        sortedStack = Stack()

        while not self.stack.is_empty():
            # Pop the top element from the input stack
            temp = self.stack.pop()

            # Move elements from sortedStack back to inputStack if they are greater than temp
            while not sortedStack.is_empty() and sortedStack.peek() > temp:
                self.stack.push(sortedStack.pop())

            # Push temp onto the sortedStack
            sortedStack.push(temp)

        # Return the sorted stack
        return sortedStack





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
    
    def __str__(self):
        """Return a user-friendly string representation of the stack"""
        return f"Current Stack: {self.stack}"    

    def sort_stack(self):
        """Sort a stack using one additional stack"""
        print("Sorting the stack...")
        sorted_stack = Stack()  # Temporary stack for sorting

        # Step 1: Sort elements using sorted_stack
        while not self.is_empty():
            temp = self.pop()
            print(f"Popped: {temp} from self")

            while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
                moved_item = sorted_stack.pop()
                print(f"Moved {moved_item} back to self")
                self.push(moved_item)

            sorted_stack.push(temp)
            # print(f"Pushed: {temp} to sorted_stack")
            # print(sorted_stack)

        # Step 2: Move elements back to the original stack
        while not sorted_stack.is_empty():
            moved_item = sorted_stack.pop()
            self.push(moved_item)
            print(self)


 
       
        





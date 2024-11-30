class Array:
    def __init__(self):
        """Initialize an empty array."""
        self.array = []

    def add(self, value):
        """Add an element to the end of the array."""
        self.array.append(value)

    def get(self, index):
        """Get the value at a specific index."""
        if 0 <= index < len(self.array):
            return self.array[index]
        else:
            raise IndexError("Index out of range")

    def update(self, index, value):
        """Update the value at a specific index."""
        if 0 <= index < len(self.array):
            self.array[index] = value
        else:
            raise IndexError("Index out of range")

    def remove(self, index):
        """Remove an element at a specific index."""
        if 0 <= index < len(self.array):
            self.array.pop(index)
        else:
            raise IndexError("Index out of range")

    def size(self):
        """Return the current size of the array."""
        return len(self.array)

    def display(self):
        """Display the elements of the array."""
        print(self.array)



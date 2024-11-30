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


# Example Usage
infinite_array = Array()

# Adding elements continuously
infinite_array.add(10)
infinite_array.add(20)
infinite_array.add(30)

# Display the array
print("Array after adding elements:")
infinite_array.display()

# Access an element
print("\nElement at index 1:", infinite_array.get(1))

# Update an element
infinite_array.update(1, 50)
print("\nArray after updating index 1 to 50:")
infinite_array.display()

# Remove an element
infinite_array.remove(0)
print("\nArray after removing element at index 0:")
infinite_array.display()

# Checking size
print("\nCurrent size of the array:", infinite_array.size())

# Adding more elements to simulate infinite growth
for i in range(1000):  # Add 1000 elements to simulate growth
    infinite_array.add(i)

print("\nArray size after adding 1000 more elements:", infinite_array.size())

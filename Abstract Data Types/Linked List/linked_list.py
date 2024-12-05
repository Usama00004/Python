from node import Node

class LinkedList:
    """A singly linked list."""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Add a new node at the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete the first occurrence of a node with the given data."""
        if self.is_empty():
            print("List is empty. Cannot delete.")
            return

        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Find the node to delete
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print("Data not found in the list.")
        else:
            current.next = current.next.next

    def display(self):
        """Display all nodes in the list."""
        if self.is_empty():
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
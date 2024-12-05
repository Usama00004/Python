from linked_list import LinkedList

def menu():
    """Menu-driven interface for LinkedList."""
    linked_list = LinkedList()
    while True:
        print("\n--- Linked List Operations Menu ---")
        print("1. Append an element")
        print("2. Prepend an element")
        print("3. Delete an element")
        print("4. Display the linked list")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            data = input("Enter the element to append: ")
            linked_list.append(int(data))
            print(f"{data} has been appended to the list.")

        elif choice == '2':
            data = input("Enter the element to prepend: ")
            linked_list.prepend(int(data))
            print(f"{data} has been prepended to the list.")

        elif choice == '3':
            data = input("Enter the element to delete: ")
            linked_list.delete(int(data))

        elif choice == '4':
            print("Current Linked List:")
            linked_list.display()

        elif choice == '5':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()

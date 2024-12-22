from node import Node
from linked_list import LinkedList

if __name__ == "__main__":
    # Initialize the LinkedList
    ll = LinkedList()
    
    while True:
        print("\nWelcome to LinkedList Operations")
        print("1. Insert at Head")
        print("2. Append")
        print("3. Insert After")
        print("4. Delete Head")
        print("5. Pop (Delete Last Element)")
        print("6. Remove Element")
        print("7. Search for Element")
        print("8. Display LinkedList")
        print("9. Clear LinkedList")
        print("10. Exit")
        
        try:
            option = int(input("Please enter your option: "))
            
            if option == 1:
                val = input("Enter the value to insert at the head: ")
                ll.insert_head(val)
                print(f"Inserted {val} at the head.")
            
            elif option == 2:
                val = input("Enter the value to append: ")
                ll.append(val)
                print(f"Appended {val} to the linked list.")
            
            elif option == 3:
                val = input("Enter the value to insert: ")
                after = input("Enter the value after which to insert: ")
                result = ll.insert_after(val, after)
                if result:
                    print(result)
                else:
                    print(f"Inserted {val} after {after}.")
            
            elif option == 4:
                result = ll.delete_head()
                if result:
                    print(result)
                else:
                    print("Deleted the head element.")
            
            elif option == 5:
                result = ll.pop()
                if result:
                    print(result)
                else:
                    print("Deleted the last element.")
            
            elif option == 6:
                val = input("Enter the value to remove: ")
                result = ll.remove(val)
                if result:
                    print(result)
                else:
                    print(f"Removed {val} from the linked list.")
            
            elif option == 7:
                val = input("Enter the value to search for: ")
                position = ll.search(val)
                if position == 'Not Found':
                    print(f"Element {val} not found in the linked list.")
                else:
                    print(f"Element {val} found at position {position + 1}.")
            
            elif option == 8:
                print("Current LinkedList:")
                print(ll)
            
            elif option == 9:
                ll.clear()
                print("Cleared the linked list.")
            
            elif option == 10:
                print("Exiting program. Goodbye!")
                break
            
            else:
                print("Invalid option! Please enter a valid option.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print(f"Unexpected error: {e}")

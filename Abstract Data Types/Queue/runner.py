def queue_runner():
    """Runner function for interacting with the Queue"""
    queue = Queue()
    print("Welcome to the Queue Program!")
    
    while True:
        print("\nSelect an option:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display Queue")
        print("5. Check if Empty")
        print("6. Get Size")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                item = input("Enter the item to enqueue: ")
                queue.enqueue(item)
            
            elif choice == 2:
                queue.dequeue()
            
            elif choice == 3:
                print(f"Front item: {queue.peek()}")
            
            elif choice == 4:
                queue.display()
            
            elif choice == 5:
                if queue.is_empty():
                    print("The queue is empty.")
                else:
                    print("The queue is not empty.")
            
            elif choice == 6:
                print(f"Size of the queue: {queue.size()}")
            
            elif choice == 7:
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a valid option.")
        
        except ValueError:
            print("Please enter a valid number.")
        except IndexError as e:
            print(e)

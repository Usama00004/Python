from stack import Stack
# Question: Given a string containing parentheses, write a function to check if the parentheses are balanced
# Question: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Question: Given an unsorted stack, sort the stack using only one additional stack. You cannot use any other data structures.


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\nWelcome to Stack")
        print(" To Push Element Press 1  \n To Pop Element Press 2 \n To Display Stack Press 3 \n To Display Length Press 4\n To sort stack press 5 \n To Exit Press 6")
        user_input = input("Please Enter your Option: ")
        try:
            option = int(user_input)
            if option == 1:
                val = input("Please enter a number which you want to push: ")
                stack.push(val)
                print("Item added successfully!")
            elif option == 2:
                item = stack.pop()
                print("Item removed successfully!")
            elif option == 3:
                print("Current Stack:")
                stack.display()
            elif option == 4:
                print(f"Current length of Stack : {stack.size()}")
            elif option == 5:
                print("1st Check")
                sortedStack = stack.sort_stack()
            elif option == 6:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option! Please enter a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")
        except IndexError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")





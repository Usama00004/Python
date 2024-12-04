from stack import Stack
# Question: Given a string containing parentheses, write a function to check if the parentheses are balanced
# Question: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Question: Given an unsorted stack, sort the stack using only one additional stack. You cannot use any other data structures.
def sort_stack(inputStack):
    sortedStack = []
    while inputStack:
        # Pop the top element from the input stack
        temp = inputStack.pop()
        # Move elements from sortedStack back to inputStack if they are greater than temp
        while sortedStack and sortedStack[-1] > temp:
            inputStack.append(sortedStack.pop()) 
        # Push temp onto the sortedStack
        sortedStack.append(temp)
    # At this point, sortedStack has the elements sorted in ascending order
    return sortedStack


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\nWelcome to Stack")
        print(" To Push Element Press 1  \n To Pop Element Press 2 \n To Display Stack Press 3 \n To Display Length Press 4\n To Exit Press 5")
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






    inputStack = [34, 3, 31, 98, 92, 23]
    sortedStack = sort_stack(inputStack)
    print("Sorted Stack:", sortedStack)
from stack import Stack

if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\nWelcome to Stack")
        print(" To Add Element Press 1 \n To Remove Element Press 2 \n To Display Array Press 3 \n To Exit Press 4")
        user_input = input("Please Enter your Option: ")



    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print(f"Top Element: {stack.peek()}")
    stack.pop()
    stack.display()
    print(f"Is Stack Empty? {stack.is_empty()}")
    print(f"Stack Size: {stack.size()}")

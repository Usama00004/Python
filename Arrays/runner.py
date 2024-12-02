from array import Array, add_element, remove_element, display_arr

if __name__ == "__main__":
    # Initialize the Array
    arr = Array()
    while True:
        print("\nWelcome")
        print(" To Add Element Press 1 \n To Remove Element Press 2 \n To Display Array Press 3 \n To Exit Press 4")
        user_input = input("Please Enter your Option: ")
        try:
            option = int(user_input)
            if option == 1:
                val = input("Please enter a number which you want to add: ")
                add_element(arr, val)
                print("Element added successfully!")
            elif option == 2:
                pos = int(input("Please enter the position of the element you want to remove: "))
                remove_element(arr, pos - 1)
                print("Element removed successfully!")
            elif option == 3:
                print("Current Array:")
                display_arr(arr)
            elif option == 4:
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

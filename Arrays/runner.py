from array import Array

if __name__ == "__main__":
    # Initialize the Array
    arr = Array()
    print("Welcome")
    print(" To Add Element Press 1 \n To Remove element Press 2 \n To Display Array Press 3 \n ")
    input("Please Enter your Option :")
    
    # Add elements to the array
    arr.add(10)
    arr.add(20)
    arr.add(30)
    print("After adding elements:")
    arr.display()
    
    # Get an element at a specific index
    print(f"Element at index 1: {arr.get(1)}")
    
    # Update an element at a specific index
    arr.update(1, 25)
    print("After updating index 1:")
    arr.display()
    
    # Remove an element
    arr.remove(0)
    print("After removing element at index 0:")
    arr.display()
    
    # Display the size of the array
    print(f"Array size: {arr.size()}")

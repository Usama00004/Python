from array import Array
  
def add_element(arr,val):
    arr.add(val)
    return arr    

def remove_element(arr,index):
    arr.remove(index)
    return arr    

def update_element(arr,index,val):
    arr.update(index,val)
    return arr 

def display_arr(arr):
    arr.display(arr)  


if __name__ == "__main__":
    # Initialize the Array
    arr = Array()
    while True:
        print("Welcome")
        print(" To Add Element Press 1 \n To Remove element Press 2 \n To Display Array Press 3\n")
        user_input = input("Please Enter your Option :")
        option = int(user_input)
        if option == 1:
            val = input("Please enter a number which you want to add :")
            array = add_element(arr,val)
            print(array)
        elif option == 2:
            pos = input("Please enter a position of element which you want to remove :")
            array = remove_element(arr,pos-1)
            print(array)
        elif option == 3:
            print(arr)
        else:
            raise Exception("Invalid option! Please enter a valid option.")  




    

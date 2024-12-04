from array import *

#Declearing an array
array_1 = array('i', [1,2,3,4,5,6,7,8,9])

#Accessing array elements
# print(array_1[3])

#Insertion in array 
array_1.insert(1,60)

#Deletion in array 
array_1.remove(5)

#Searching in an array
print(array_1.index(60))

#Updation in an array 
array_1[2] = 100

# Iterating over an array
for x in array_1:
    print(x)


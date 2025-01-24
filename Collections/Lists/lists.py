# # Declearing List 
# list1 = ['physics','Chemistry',1997,2008]
# list2 = [1,2,3,4,5,6,7]


# # Declearing List
# list1 = ['physics','chemistry',1997,2000]
# list2 = [1,2,3,4,5,6,7]

# #Accessing List Values
# print ("list[0]: ", list1[0])
# print ("list2[1:5] :", list2[1:5])

# #Updating Lists Values
# list1[2] = 2001
# print("printing list after updating index 2",list1)

# #Deleting List Values
# del list1[2]
# print("printing list after deleting index 2",list1)


# #Basic list Operations
# #Length 
# print(len(list1))

# #Concatination
# print(list1+list2)

# #Repetation
# print(['Hi']*4)

# #Membership
# 3 in [1,2,43,4,5]

# #Iteration
# for x in [1,2,3,4,5]:
#     print(x)

##############
## Create a list
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [11,12,13,14,15,16,17,18,19,20]

## Append to a list
list_2.append(21)

## Extending a list with another list
list_1.extend(list_2)

## Inserting at a specific index
list_1.insert(0,0)

## Removing an element from a list
list_1.remove(0)


## Poping an element from a list (Remove that element from List)
element = list_1.pop()
print(element)
print(list_1)


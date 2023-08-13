"""
- Insertion sort is not a fast Sorting Algorithm
- It Uses nested loops to sort
- It is useful only for small datasets
- It runs in O(n^2)

"""

list_to_be_sorted=[2,8,6,7,5,9,8,3,7,8,6,]
def insertion_sort(list):
    for i in range(1,len(list)):
        for j in range(i-1,0,-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
            else:
                break    
    return list

sorted_list = insertion_sort(list_to_be_sorted)
print(sorted_list)


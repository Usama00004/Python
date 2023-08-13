"""
- Insertion sort is not a fast Sorting Algorithm
- It Uses nested loops to sort
- It is useful only for small datasets
- It runs in O(n^2)

"""
list_to_be_sorted=[2,8,6,7,5,9,8,3,7,8,6]
def selection_sort(list):
    for i in range (0,len(list)-1):
        min_index = i
        for j in range (i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[i],list[min_index] = list[min_index], list[i]
    return list

sorted_list = selection_sort(list_to_be_sorted)
print(sorted_list)





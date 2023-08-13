list_to_be_sorted=[2,8,6,7,5,9,8,3,7,8,6,]
def bubble_sort(list):
    for i in range(0,len(list)-1):
        for j in range(0,len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list
sorted_list = bubble_sort(list_to_be_sorted)
print(sorted_list)

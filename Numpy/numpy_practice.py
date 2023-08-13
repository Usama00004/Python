import numpy as np

print(np.__version__)

# Methods for Creating Numpy arrays
arr_1 = np.array([1,2,3,4,5,6,7,8])

arr_2 = np.zeros((3,3))

arr_3 = np.ones((3,3))

arr_4 = np.identity(5)

arr_5 = np.arange(10)

arr_6 = np.arange(5,16)

arr_7 = np.arange(5,16,3)

arr_8 = np.linspace(10,20,10)

arr_9 = arr_5.copy()

#Changing datatype of elements in Array
arr_10 = arr_5.astype('float')

#Shape of Array 
print(arr_1.shape)

#Dimension of Array
print(arr_2.ndim)

#size of array
print(arr_3.size)

#Item Size(size occupied by each item in menory)
print(arr_4.itemsize)

#Data type of each element in Array
print(arr_5.dtype)



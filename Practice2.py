import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# 0-D Arrays


#1-D Array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#2-D Array
arr = np.array([[1,2,3], [4,5,6]])
print(arr)

#nDims example:
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#Higher dimensional arrays
arr = np.array([1, 2, 3, 4], ndim = 5)
print(arr)
print("Number of dimensions : ", arr.ndim)

#Slicing arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])
print(arr[4:1])
print(arr[:4])

#Negative slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

#Slicing 2D arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#Shaping arrays
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#Reshaping arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

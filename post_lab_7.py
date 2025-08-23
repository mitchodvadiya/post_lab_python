import numpy as np
from numpy import linalg as LA

# Example 1: Create array from list
list1 = [2, 4, 6, 8]
array1 = np.array(list1)
print(array1)

# Example 2: Direct array creation
array1 = np.array([2, 4, 6, 8])
print(array1)

# Example 3: Using np.zeros()
array1 = np.zeros(4)
print(array1)

# Example 4: Using np.arange()
array1 = np.arange(5)
print("Using np.arange(5):", array1)
array2 = np.arange(1, 9, 2)
print("Using np.arange(1, 9, 2):", array2)

# Example 5: Using np.random.rand()
array1 = np.random.rand(5)
print(array1)

# Task Example 1: 1D array
arr1 = np.array([10, 20, 30])
print("My 1D array:\n", arr1)

# Task Example 2: 2D array
arr2 = np.array([[10, 20, 30], [40, 50, 60]])
print("My 2D numpy array:\n", arr2)

# Task Example 3: Sequential array with steps
arr = np.arange(0, 20, 3)
print("A sequential array with steps of 3:\n", arr)

# Task Example 4: Sequential array with linspace
arr = np.linspace(0, 3, 5)
print("A sequential array with 5 values between 0 and 5:\n", arr)

# Task Example 8: ones() array
arr = np.ones((2, 3))
print("numpy array:\n", arr)
print("Type:", type(arr))

# Check Data Type
int_array = np.array([-3, -1, 0, 1])
float_array = np.array([0.1, 0.2, 0.3])
complex_array = np.array([1+2j, 2+3j, 3+4j])
print(int_array.dtype)
print(float_array.dtype)
print(complex_array.dtype)

# Creating arrays with defined dtype
array1 = np.array([1, 3, 7], dtype='int8')
array2 = np.array([2, 4, 6], dtype='uint16')
array3 = np.array([1.2, 2.3, 3.4], dtype='float32')
array4 = np.array([1+2j, 2+3j, 3+4j], dtype='complex64')
print(array1, array1.dtype)
print(array2, array2.dtype)
print(array3, array3.dtype)
print(array4, array4.dtype)

# Type Conversion
int_array = np.array([1, 3, 5, 7])
float_array = int_array.astype('float')
print(int_array, int_array.dtype)
print(float_array, float_array.dtype)

# ndim Attribute
array1 = np.array([[2, 4, 6],
                   [1, 3, 5]])
print(array1.ndim)

# size Attribute
array1 = np.array([[1, 2, 3],
                   [6, 7, 8]])
print(array1.size)

# shape Attribute
array1 = np.array([[1, 2, 3],
                   [6, 7, 8]])
print(array1.shape)

# dtype Attribute
array1 = np.array([6, 7, 8])
print(array1.dtype)

# itemsize Attribute
array1 = np.array([6, 7, 8, 10, 13])
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32)
print(array1.itemsize)
print(array2.itemsize)

# data Attribute
array1 = np.array([6, 7, 8])
array2 = np.array([[1, 2, 3],
                   [6, 7, 8]])
print("\nData of array1 is: ", array1.data)
print("Data of array2 is: ", array2.data)

# Matrix Multiplication
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("Original matrices:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the matrix multiplication:")
print(result1)

# Determinant
a = np.array([[1, 0], [1, 2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))


# -------------------------------------------------------------------------------------------------------------

# post_lab_7

import numpy as np

# a. Create a 3x3 matrix with values from 2 to 10
matrix = np.arange(2, 11).reshape(3, 3)
print("a. 3x3 Matrix:")
print(matrix)

# b. Reverse an array
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print("\nb. Reversed Array:", reversed_arr)

# c. Find common values between two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
common_values = np.intersect1d(arr1, arr2)
print("\nc. Common Values:", common_values)

# d. Repeat array elements
arr3 = np.array([1, 2, 3])
repeated = np.repeat(arr3, 3)
print("\nd. Repeated Elements:", repeated)

# e. Find the memory size of a NumPy array
arr4 = np.array([10, 20, 30, 40, 50])
print("\ne. Memory Size of array:", arr4.nbytes, "bytes")

# f. Create an array of ones and zeros
ones_array = np.ones((2, 3))
zeros_array = np.zeros((2, 3))
print("\nf. Ones Array:\n", ones_array)
print("Zeros Array:\n", zeros_array)

# g. Find the 4th element of an array
arr5 = np.array([11, 22, 33, 44, 55, 66])
print("\ng. 4th Element:", arr5[3])   


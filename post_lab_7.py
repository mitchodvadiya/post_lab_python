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



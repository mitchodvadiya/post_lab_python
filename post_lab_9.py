# post_lab_9..

# Post Lab Exercise – Pandas Programs

import pandas as pd
import numpy as np

# (a) Add, Subtract, Multiply and Divide two Series
s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([1, 2, 3, 4])

print("Series 1:")
print(s1)
print("\nSeries 2:")
print(s2)

print("\nAddition:")
print(s1 + s2)

print("\nSubtraction:")
print(s1 - s2)

print("\nMultiplication:")
print(s1 * s2)

print("\nDivision:")
print(s1 / s2)

# (b) Convert dictionary to Pandas Series
data = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(data)
print("\nDictionary to Series:")
print(series_from_dict)

# (c) Create Series from List, NumPy Array, and Dictionary
list_data = [10, 20, 30, 40]
series_list = pd.Series(list_data)
print("\nSeries from List:")
print(series_list)

array_data = np.array([5, 15, 25, 35])
series_array = pd.Series(array_data)
print("\nSeries from NumPy Array:")
print(series_array)

dict_data = {'x': 1, 'y': 2, 'z': 3}
series_dict = pd.Series(dict_data)
print("\nSeries from Dictionary:")
print(series_dict)

# (d) Stack two Series vertically and horizontally
s3 = pd.Series([1, 2, 3])
s4 = pd.Series([4, 5, 6])

print("\nSeries 1 for stacking:")
print(s3)
print("\nSeries 2 for stacking:")
print(s4)

vertical_stack = pd.concat([s3, s4])
print("\nVertical Stack:")
print(vertical_stack)

horizontal_stack = pd.concat([s3, s4], axis=1)
print("\nHorizontal Stack:")
print(horizontal_stack)



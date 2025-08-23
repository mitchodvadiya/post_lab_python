import pandas as pd
import numpy as np

# Series Examples

print("=== Series Example ===")
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

# Arithmetic Operations
series2 = series + 10
print("\nSeries + 10:")
print(series2)

# Filtering
filtered_series = series[series > 2]
print("\nFiltered Series (>2):")
print(filtered_series)

# Statistical Calculations
mean_value = series.mean()
print("\nMean Value of Series:", mean_value)


# DataFrame Examples
print("\n=== DataFrame Example ===")
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# Accessing Columns
print("\nAccessing 'Name' column:")
print(df[['Name']])

# Adding a New Column
df['Salary'] = [70000, 80000, 90000]
print("\nAfter Adding Salary Column:")
print(df)

# Dropping a Column
df = df.drop('City', axis=1)
print("\nAfter Dropping City Column:")
print(df)

# Row Selection
print("\nReturn row 0:")
print(df.loc[[0]])

print("\nReturn row 0 and 1:")
print(df.loc[[0, 1]])

# Named Index Example
print("\n=== Named Index Example ===")
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)


# Reading and Writing Data
print("\n=== Reading and Writing Example ===")
# Example Data
Biodata = {
    'Name': ['John', 'Emily', 'Mike', 'Lisa'],
    'Age': [28, 23, 35, 31],
    'Gender': ['M', 'F', 'M', 'F']
}
df = pd.DataFrame(Biodata)

# Save to CSV
df.to_csv('Biodata.csv', index=False)
print("Biodata DataFrame saved to 'Biodata.csv'")

# Read back CSV (if file exists in your directory)
dat = pd.read_csv("Biodata.csv")
print("\nRead CSV:")
print(dat)


# Data Inspection
print("\n=== Data Inspection ===")
print(dat.info())
print(dat.head())
print(dat.tail())
print(dat.describe())


# Data Selection and Indexing
print("\n=== Data Selection and Indexing ===")
print(dat[['Name']])
print(dat[['Name', 'Age']])
print(dat.loc[[1]])


# Task: Create DataFrame with Numeric Columns
print("\n=== Task: Numeric Columns DataFrame ===")
data = {
    'A': [np.nan, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': np.random.normal(50, 15, 10),
    'C': np.random.rand(10) * 100,
    'D': np.linspace(1, 10, 10),
    'E': np.logspace(1, 2, 10)
}
df = pd.DataFrame(data)
print(df)


# ------------------------------------------------------------------------------------------------------------------

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


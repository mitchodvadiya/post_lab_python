# a. Write a Python program to draw a line with suitable label in the x axis, y axis and a title.

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [8, 5, 10, 15, 19]
plt.plot(x, y)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Graph")
plt.show()

# b. Write a Python program to plot two or more lines on same plot with suitable legends of each line.

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
y3 = [2, 3, 4, 5, 6]
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.plot(x, y3, label="Line 3")

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines Example")
plt.legend()
plt.show()

# Write a Python programming to display a bar chart of the popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Plot bar chart
plt.bar(languages, popularity)

# Labels and title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Popularity of Programming Languages")

plt.show()
